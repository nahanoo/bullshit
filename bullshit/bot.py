from bullshit import Bullshit
from bullshit import Player
import names
import random
import scipy
import scipy.stats
import statsmodels.stats.proportion

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
    
    def get_max_confident_count(dices_in_round):
        x = scipy.linspace(0,i,i+1)
        pmf = scipy.stats.binom.pmf(x,i,1/3)
        for d,p in enumerate(pmf):
            if p >= 0.2:
                confident_count_estimate = d
        return confident_count_estimate

    def make_game_move(self,game_round):
        bluff = random.choice(3*[False]+[True])
        if game_round.moves == 0:
            if not bluff:
                self.guess_dice_number = self.get_most_frequent_dice_number()
                self.guess_dice_count = random.choice(range(1,self.get_max_confident_count(game_round.dices_in_round)))
            if bluff:
                self.guess_dice_number = random.randint(1,6)
                self.guess_dice_count = random.choice(range(1,self.get_max_confident_count(game_round.dices_in_round)))

