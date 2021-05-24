from bullshit import Bullshit
from bullshit import Player
import names
import random

class Bot(Player):
    def __init__(self,n_dices_per_player):
        super().__init__(n_dices_per_player)

    def get_most_frequent_dice_number(self):
        dice_counts = dict()
        for dice_number in self.dices.values():
            if dice_number != 1:
                try:
                    dice_counts[dice_number] += 1
                except KeyError:
                    dice_counts[dice_number] = 1
        for dice_number in self.dices.values():
            if dice_number == 1:
                if len(dice_counts) > 0:
                    for dice_number in dice_counts:
                        dice_counts[dice_number] += 1
                else:
                    dice_counts[dice_number] = 1
        return max(dice_counts,key=dice_counts.get)

    def make_game_move(self,game_round):
        bluff = random.choice(3*[False]+[True])
        if game_round.moves == 0:
            if not bluff:
                self.guess_dice_number = self.get_most_frequent_dice_number()

