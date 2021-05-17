from bullshit import Bullshit
import names

class Bott:
    def __init__(self,n_dices_per_player):
        self.bot = True
        self.name = names.get_first_name()
        self.participates = True
        self.n_dices_per_player = n_dices_per_player
        self.dices = dict()
        for n in range(self.n_dices_per_player):
            self.dices[n] = Bullshit.Player.Dice()
        self.guess = Bullshit.Player.Guess()

    def get_most_frequent_dice_number(self):
        dice_counts = dict()
        for dice_number in [dice.dice_number for dice in self.dices.values()]:
            if dice_number != 1:
                try:
                    dice_counts[dice_number] += 1
                except KeyError:
                    dice_counts[dice_number] = 1
        for dice_number in [dice.dice_number for dice in self.dices.values()]:
            if dice_number == 1:
                if len(dice_counts) > 0:
                    for dice_number in dice_counts:
                        dice_counts[dice_number] += 1
                else:
                    dice_counts[dice_number] = 1
        return max(dice_counts,key=dice_counts.get)
