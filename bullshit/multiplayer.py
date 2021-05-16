from .bullshit import Bullshit
from .interface import Interface

def get_players(players):
    for player in players.values():
        player.name = input('Enter the name of the player:\n')
        player.participates = True

def get_guess(player):
    def get_dice_number(player):
        dice_number = input(player.name+' ,which dice number do you estimate?\n')
        return dice_number

    def get_dice_count(player):
        dice_count = input(player.name+' ,how many ',+str(player.Guess.dice_number)+'s are in this round?\n')
        return dice_count
        
    dice_number = get_dice_number(player)
    if type(dice_number) != int:
            print('You did not enter a number. Only numbers are allowed.')
            get_dice_number(player)
    else:
        player.Guess.dice_number = dice_number
    
    dice_count = get_dice_count(player)
    if type(dice_count) != int:
            print('You did not enter a number. Only numbers are allowed.')
            get_dice_count(player)
    else:
        player.Guess.dice_count = dice_count
    

def main(n_players,n_dices_per_person):
    game = Bullshit()
    interface = Interface()
    game.running = True
    game.Players = game.create_players(2,3)
    get_players(game.players)
    rounds = []
    while game.running is True:
        for player in game.players.values():
            player.roll_dices()
            interface.show_dices(player)
            get_guess(player)



    return game
