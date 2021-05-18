from bullshit import Bullshit
from bullshit import Player
from bullshit import Round
from bullshit import Interface

def get_player_names(players):
    for player in players.values():
        player.name = input('Enter the name of the player: ')
        player.participates = True

def get_guess(player):
    def get_dice_number(player):
        dice_number = input('Which dice number do you pick to make a guess?\n')
        return dice_number

    def get_dice_count(player):
        dice_count = input('How many '+str(player.guess_dice_number)+'s do you estimate are in this round?\n')
        return dice_count

    valid_dice_number = False
    while valid_dice_number is False:
        dice_number = get_dice_number(player)
        try:
            int(dice_number)
            player.guess_dice_number = int(dice_number)
            valid_dice_number = True
        except ValueError:
            print('You did not enter a number. Only numbers are allowed.')
            pass
    
    valid_dice_count = False
    while valid_dice_count is False:
        dice_count = get_dice_count(player)
        try:
            int(dice_count)
            player.guess_dice_count = int(dice_count)
            valid_dice_count = True
        except ValueError:
            print('You did not enter a number. Only numbers are allowed.')
            pass    

def main(n_players,n_dices_per_person):
    game = Bullshit()
    interface = Interface()
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
                    valid_decision = False
                    print('Player '+player.name+':')
                    while valid_decision is False:
                        decision = input('Press s to show dices, b to call Bullshit, or g to make a Guess. ')
                        if decision == 's':
                            interface.show_dices(player)
                        if decision == 'g':
                            get_guess(player)
                            valid_decision = True
                        if decision == 'b':
                            previous_player = game_round.player_order[game_round.player_order.index(key)-1]
                            bullshit = game.check_bullshit(players,players[previous_player])
                            if not bullshit:
                                print('Ha! No bullshit - the guess was correct.')
                                if len(players[key].dices) >= 1:
                                    players[key].dices.popitem()
                                if len(players[key].dices) == 0:
                                    players[key].participates = False
                                    game.active_players -= 1
                                    print('That was your last dice. You are out!')
                                looser = key
                            if bullshit:
                                print('Correct! Do not trust your friends, it was bullshit.')
                                if len(players[previous_player].dices) >= 1:
                                    players[previous_player].dices.popitem()
                                if len(players[previous_player].dices) == 0:
                                    players[previous_player].participates = False
                                    game.active_players -= 1
                                    print('That was the last dice of '+players[previous_player].name+'. You are out!')
                                looser = previous_player
                            game_round.running = False
                            valid_decision = True
                        else:
                            pass

        if game.active_players == 1:
            for player in players.values():
                if player.participates:
                    print('Congratulations '+player.name+', you won.')
                    game.running = False

        else:
            if players[looser].participates:
                players = game.change_player_order(players,looser)
            else:
                if game_round.player_order.index(players,looser) == len(game_round.player_order) -1:
                    players = game.change_player_order(game_round.player_order[0])
                else:
                    next_player = game_round.player_order[game_round.player_order.index(looser)+1]
                    players = game.change_player_order(players,next_player)
    return game