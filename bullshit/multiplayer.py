from bullshit import Bullshit
from bullshit import Player
from bullshit import Round
from bullshit import Interface

def get_player_names(players):
    for player in players.values():
        player.name = input('Enter the name of the player: ')
        player.participates = True

def main(n_players,n_dices_per_person):
    game = Bullshit()
    game.running = True
    players = game.create_players(n_players,n_dices_per_person)
    game.active_players = n_players
    get_player_names(players)
    while game.running is True:
        game_round = Round()
        game_round.running = True
        for key,player in players.items():
            if player.participates:
                game_round.player_order.append(key)
        for player in players.values():
                player.roll_dices()
        while game_round.running:
            for key,player in players.items():
                if (player.participates and game_round.running):                
                    print('Player '+player.name+':')
                    looser = player.make_game_move(game,game_round,players)
                    if looser:
                        game_round.running = False
                    game_round.moves += 1
        if game.active_players == 1:
            for player in players.values():
                if player.participates:
                    print('Congratulations '+player.name+', you won.')
                    game.running = False
        else:
            if players[looser].participates:
                players = game.change_player_order(players,looser)
            else:
                next_player = game_round.get_next_player(looser)
                players = game.change_player_order(players,next_player)
    return game