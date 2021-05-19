import random
from bullshit import Interface

class Bullshit:
    """Bullshit dice game engine"""
    def __init__(self):
        self.running = False
        self.active_players = 0
        self.bot = False

    def create_players(self,n_players,n_dices_per_player):
        """Create muliplte players with n dices per player"""
        players = dict()
        for n in range(n_players):
            player_id = 'player_'+str(n)
            players[player_id] = Player(n_dices_per_player)
            players[player_id].player_id = player_id
        return players

    def check_bullshit(self,players,guesser):
        """Check if estimate of a player is bullshit"""
        dice_count = 0
        for player in players.values():
            for dice in player.dices.values():
                if dice == guesser.guess_dice_number or dice == 1:
                    dice_count += 1
        if dice_count >= guesser.guess_dice_count:
            return False
        else:
            return True

    def change_player_order(self,players,looser):
        names = list(players.keys())
        reordered_names = []
        looser_index = names.index(looser)
        for i in range(looser_index,len(names)):
            reordered_names.append(names[i])
        for i in range(looser_index):
            reordered_names.append(names[i])
        previous_player_order = players
        players = dict()
        for name in reordered_names:
            players[name] = previous_player_order[name]
        return players
   
class Player:
    """A player which has dices, an guess and some helper functions"""
    def __init__(self,n_dices_per_player):
        
        # Player is still in round
        self.participates = True

        # Name of a player and dices of a person
        self.name = None
        self.player_id = None
        self.n_dices_per_player = n_dices_per_player

        # Create dices of a player
        self.dices = dict()
        for n in range(self.n_dices_per_player):
            self.dices[n] = None

        # Create guess
        self.guess_dice_number = None
        self.guess_dice_count = None

    def roll_dices(self):
        """Roll the dices of a player"""
        for dice in self.dices:
                self.dices[dice] = random.randint(1,6)

    def print_throw(self):
        """Print the throw of a player"""
        dices = [str(dice) for dice in self.dices.values()]
        print(''.join(['|','|'.join(dices),'|']))

    def get_guess(self):
        def get_dice_number(self):
            dice_number = input('Which dice number do you pick to make a guess?\n')
            return dice_number

        def get_dice_count(self):
            dice_count = input('How many '+str(self.guess_dice_number)+'s do you estimate are in this round?\n')
            return dice_count

        valid_dice_number = False
        while valid_dice_number is False:
            dice_number = get_dice_number(self)
            try:
                int(dice_number)
                self.guess_dice_number = int(dice_number)
                valid_dice_number = True
            except ValueError:
                print('You did not enter a number. Only numbers are allowed.')
                pass
        
        valid_dice_count = False
        while valid_dice_count is False:
            dice_count = get_dice_count(self)
            try:
                int(dice_count)
                self.guess_dice_count = int(dice_count)
                valid_dice_count = True
            except ValueError:
                print('You did not enter a number. Only numbers are allowed.')
                pass

    def check_guess(self,previous_player):
        pass

    def make_game_move(self,game,game_round,players):
        valid_decision = False
        previous_player = game_round.get_previous_player(self.player_id)
        while valid_decision is False:
            decision = input('Press s to show dices, b to call Bullshit, or g to make a Guess. ')
            if decision == 's':
                interface = Interface()
                interface.show_dices(self)
            if decision == 'g':
                self.get_guess()  
                valid_decision = True
            if decision == 'b':
                bullshit = game.check_bullshit(players,players[previous_player])
                if not bullshit:
                    print('Ha! No bullshit - the guess was correct.')
                    if len(self.dices) >= 1:
                        self.dices.popitem()
                    if len(self.dices) == 0:
                        self.participates = False
                        game.active_players -= 1
                        print('That was your last dice. You are out!')
                    return self.name_id
                if bullshit:
                    print('Correct! Do not trust your friends, it was bullshit.')
                    if len(players[previous_player].dices) >= 1:
                        players[previous_player].dices.popitem()
                    if len(players[previous_player].dices) == 0:
                        players[previous_player].participates = False
                        game.active_players -= 1
                        print('That was the last dice of '+players[previous_player].name+'. You are out!')
                    return previous_player
                valid_decision = True

class Round:
        def __init__(self):
            self.moves = 0
            self.running = None
            self.player_order = []

        def get_previous_player(self,current_player):
            return self.player_order[self.player_order.index(current_player)-1]

        def get_next_player(self,current_player):
            if self.player_order.index(current_player) == len(self.player_order) -1:
                    return self.player_order[0]
            else:
                return self.player_order[self.player_order.index(current_player)+1]