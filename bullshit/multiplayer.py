from bullshit import Bullshit
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
        dice_count = input('How many '+str(player.guess.dice_number)+'s do you estimate are in this round?\n')
        return dice_count

    valid_dice_number = False
    while valid_dice_number is False:
        dice_number = get_dice_number(player)
        try:
            int(dice_number)
            player.guess.dice_number = int(dice_number)
            valid_dice_number = True
        except ValueError:
            print('You did not enter a number. Only numbers are allowed.')
            pass
    
    valid_dice_count = False
    while valid_dice_count is False:
        dice_count = get_dice_count(player)
        try:
            int(dice_count)
            player.guess.dice_count = int(dice_count)
            valid_dice_count = True
        except ValueError:
            print('You did not enter a number. Only numbers are allowed.')
            pass    

def main(n_players,n_dices_per_person):
    game = Bullshit()
    interface = Interface()
    game.running = True
    game.create_players(n_players,n_dices_per_person)
    game.active_players = n_players
    get_player_names(game.players)
    while game.running is True:
        game.game_round = game.Round()
        game.game_round.running = True
        for key,player in game.players.items():
            if player.participates:
                game.game_round.player_order.append(key)
        for player in game.players.values():
                player.roll_dices()
        while game.game_round.running:
            for key,player in game.players.items():
                if (player.participates and game.game_round.running):
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
                            previous_player = game.game_round.player_order[game.game_round.player_order.index(key)-1]
                            bullshit = game.check_bullshit(game.players,game.players[previous_player])
                            if not bullshit:
                                print('Ha! No bullshit - the guess was correct.')
                                if len(game.players[key].dices) >= 1:
                                    game.players[key].dices.popitem()
                                if len(game.players[key].dices) == 0:
                                    game.players[key].participates = False
                                    game.active_players -= 1
                                    print('That was your last dice. You are out!')
                                looser = key
                            if bullshit:
                                print('Correct! Do not trust your friends, it was bullshit.')
                                if len(game.players[previous_player].dices) >= 1:
                                    game.players[previous_player].dices.popitem()
                                if len(game.players[previous_player].dices) == 0:
                                    game.players[previous_player].participates = False
                                    game.active_players -= 1
                                    print('That was the last dice of '+game.players[previous_player].name+'. You are out!')
                                    looser = previous_player
                            game.game_round.running = False
                            valid_decision = True
                        else:
                            pass

        if game.active_players == 1:
            for player in game.players.values():
                if player.participates:
                    print('Congratulations '+player.name+', you won.')
                    game.running = False

        else:
            if game.players[looser].participates:
                game.change_player_order(looser)
            else:
                if game.game_round.player_order.index(looser) == len(game.game_round.player_order) -1:
                    game.change_player_order(game.game_round.player_order[0])
                else:
                    next_player = game.game_round.player_order[game.game_round.player_order.index(looser)+1]
                    game.change_player_order(next_player)
    return game