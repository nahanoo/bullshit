from bullshit import Bullshit

def set_estimate(player):
    dice_number = input(player.name+', enter dice number: ')
    player.estimate.dice_number = int(dice_number)
    dice_count = input(player.name+', enter the estimated dice count: ')
    player.estimate.dice_count = int(dice_count)
    os.system('clear')


def game(n_players,n_dices_per_player):
    game = Bullshit()
    players = game.create_players(n_players,n_dices_per_player)
    for player in players.values():
        name = input('Enter your name: ')
        player.name = name
    #input('Ready? Press Enter to Start the game.')
    #bullshit = False
    #while bullshit == False:
    for counter,player in enumerate(players.values()):
        if player.guess.dice_number is None:
            input('Press enter to roll the dices '+player.name+'.')
            player.roll_dices()
            player.print_throw()

    return players
    """
            set_estimate(player)
        else:
            print(player.name+' your dices:')
            print_throw(player)
            b = input('Press "b" if you want to call bullshit.\n')
            if b != 'b':
                set_estimate(player)
            else:
                if check_bullshit(players,list(players.values())[counter-1]) is True:
                    print('You were right, it is bullshit.')
                if check_bullshit(players,list(players.values())[counter-1]) is False:
                    print('You were wrong it is correct')
                for player in players.values():
                    print(player.name,player.estimate.dice_count,player.estimate.dice_number)
                    print_throw(player)

                bullshit = True
                break
        
    return players
    """
p = game(2,3)