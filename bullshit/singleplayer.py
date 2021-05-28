from .bullshit import Bullshit
from .bullshit import Player
from .bot import Bot
from .bullshit import Round
from .interface import Interface


def create_bots(n_bots,n_dices_per_player):
    """A function of the game to create and return
    a dictionary of the Player class.
    The key of the dictionary is enumerated player_n.
    """
    bots = dict()
    for n in range(n_bots):
        player_id = 'player_'+str(n)
        bots[player_id] = Bot(n_dices_per_player)
        bots[player_id].player_id = player_id
    return bots

def main(n_bots,n_dices_per_player):
    """Creates and starts the game. Implements game logic of multiplayer mode.
    Players as a dictionary of Player calsses are passed to game relevant functions.
    """
    game = Bullshit()
    game.running = True
    # returns dictionary of players. Dictionary key is enumerated player_n.
    players = dict()
    player_id = 'player_0'
    players[player_id] = Player(n_dices_per_player)
    players[player_id].player_id = player_id
    game.get_player_names(players)
    for n in range(1,n_bots+1):
        player_id = 'player_'+str(n)
        players[player_id] = Bot(n_dices_per_player)
        players[player_id].player_id = player_id

    game.active_players = n_bots+1
    while game.running is True:
        dices_in_round = 0
        for player in players.values():
            if player.participates:
                dices_in_round += len(player.dices)
        print('\nThis is a new round of bullshit!\nThere are',dices_in_round,'dices in this round.')
        game_round = Round()
        # creates game round which is used mainly to keep track of player order.
        game_round.running = True
        for key,player in players.items():
            # players are not poped() from the players dictionary but inactivated
            if player.participates:
                game_round.player_order.append(key)
        for player in players.values():
                player.roll_dices()
        while game_round.running:
            for key,player in players.items():
                if (player.participates and game_round.running):
                    if player.bot is False:
                        print('\nPlayer',player.name,"it's your turn.")
                        # this function asks the player to decide if to guess or to bullshit
                        looser = player.make_game_move(game,game_round,players)
                        if looser:
                            # if bullshit is called ther has to be a looser
                            # if guess is taken looser is None
                            game_round.running = False
                        game_round.moves += 1
                    else:
                        print('\nPlayer',player.name,'is playing and has',len(player.dices),'dice(s).')
                        player.timer()
                        looser = player.make_game_move(game,game_round,players)
                        if looser:
                            game_round.running = False
                        game_round.moves += 1
        if game.active_players == 1:
            # this checks if the round has been won
            for player in players.values():
                if player.participates:
                    print('Congratulations '+player.name+', you won.')
                    game.running = False
        else:
            # if someone last the round he has not lost the game
            if players[looser].participates:
                # if the looser of the round still participates he/she starts next round
                players = game.change_player_order(players,looser)
            else:
                # if the looser lost the game the player after him starts the round
                next_player = game_round.get_next_player(looser)
                players = game.change_player_order(players,next_player)
