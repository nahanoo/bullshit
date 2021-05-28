from .bullshit import Bullshit
from .bullshit import Player
import names
import random
import scipy
import scipy.stats
import statsmodels.stats.proportion
import time
import sys

class Bot(Player):
    def __init__(self,n_dices_per_player):
        super().__init__(n_dices_per_player)
        self.bot = True
        self.name = names.get_full_name()

    def timer(self):
        for ticker in range(2):
            blah="\|/-\|/-"
            for l in blah:
                sys.stdout.write(l)
                sys.stdout.flush()
                sys.stdout.write('\b')
                time.sleep(0.2)

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
    
    def get_max_confident_count(self,players):
        dices_in_round = 0
        for player in players.values():
            if player.participates:
                dices_in_round += len(player.dices)
        x = scipy.linspace(0,dices_in_round,dices_in_round+1)
        pmf = scipy.stats.binom.pmf(x,dices_in_round,1/3)
        for d,p in enumerate(pmf):
            if p >= 0.2:
                confident_count_estimate = d
        if confident_count_estimate == 0:
            return 1
        else:
            return confident_count_estimate

    def make_game_move(self,game,game_round,players):
        bluff = random.choice(3*[False]+[True])
        if game_round.moves == 0:
            if not bluff:
                self.guess_dice_number = self.get_most_frequent_dice_number()
                self.guess_dice_count = random.choice(range(1,self.get_max_confident_count(players)+1))
            if bluff:
                self.guess_dice_number = random.randint(1,6)
                self.guess_dice_count = random.choice(range(1,self.get_max_confident_count(players)+1))
            print('Player',self.name,'guessed',self.guess_dice_count,str(self.guess_dice_number)+'s.')
        else:
            previous_player = game_round.get_previous_player(self.player_id)
            if players[previous_player].guess_dice_count > self.get_max_confident_count(players):
                bullshit = game.check_bullshit(players,players[previous_player])
                print(self.name,'called bullshit.')
                if not bullshit:
                    print('Ha! No bullshit - the guess was correct.')
                    # player looses a dice
                    self.dices.popitem()
                    if len(self.dices) == 0:
                        # if no dices are left he is out of the game.
                        self.participates = False
                        game.active_players -= 1
                        print('That was your last dice. You are out!')
                    # retunrs player id of the looser
                    return self.player_id
                if bullshit:
                    print('Correct! Do not trust your bots, it was bullshit.')
                    # previous player looses dice because of wrong guess
                    players[previous_player].dices.popitem()
                    if len(players[previous_player].dices) == 0:
                        # if it was last dice player is out of the gmae
                        players[previous_player].participates = False
                        game.active_players -= 1
                        print('That was the last dice of '+players[previous_player].name+'. You are out!')
                    return previous_player
            else:
                if not bluff:
                    self.guess_dice_number = self.get_most_frequent_dice_number()
                    self.guess_dice_count = players[previous_player].guess_dice_count + 1
                if bluff:
                    self.guess_dice_number = random.randint(1,6)
                    self.guess_dice_count = players[previous_player].guess_dice_count + 1

                print('Player',self.name,'guessed',self.guess_dice_count,str(self.guess_dice_number)+'s.')

