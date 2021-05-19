import random
from bullshit import Interface

class Bullshit:
    """This class is used to control the game status."""
    def __init__(self):
        self.running = False
        self.active_players = 0
        self.bot = False

    def create_players(self,n_players,n_dices_per_player):
        """A function of the game to create and return
        a dictionary of the Player class.
        The key of the dictionary is enumerated player_n.
        """
        players = dict()
        for n in range(n_players):
            player_id = 'player_'+str(n)
            players[player_id] = Player(n_dices_per_player)
            players[player_id].player_id = player_id
        return players

    def check_bullshit(self,players,guesser):
        """Check if estimate of a player is bullshit.
        It takes the dictionary of Player classes and the Player
        who called bullshit.
        """
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
        """If the round is lost the looser starts the round.
        If the looser of the round is out of the game the 
        Player after him starts the next round.
        """
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
    """Player class to execute game moves, store guesses
    and participation status. Game moves are execute by passing
    a dictionary of Players
    """
    def __init__(self,n_dices_per_player):
        
        # this flag is used to check participation status in game
        self.participates = True

        self.name = None
        self.player_id = None
        self.n_dices_per_player = n_dices_per_player

        # create dices of a player
        self.dices = dict()
        for n in range(self.n_dices_per_player):
            self.dices[n] = None

        # create guess to store future guesses
        self.guess_dice_number = None
        self.guess_dice_count = None

    def roll_dices(self):
        """Roll the dices of a player."""
        for dice in self.dices:
                self.dices[dice] = random.randint(1,6)

    def print_throw(self):
        """Print the throw of a player."""
        dices = [str(dice) for dice in self.dices.values()]
        print(''.join(['|','|'.join(dices),'|']))

    def get_guess(self):
        """This functions parses the number of the dice
        and the estimate n_count of the dice in the entire round.
        """
        def get_dice_number(self):
            # get dice number
            dice_number = input('Which dice number do you pick to make a guess?\n')
            return dice_number

        def get_dice_count(self):
            # get dice count
            dice_count = input('How many '+str(self.guess_dice_number)+'s do you estimate are in this round?\n')
            return dice_count

        valid_dice_number = False
        # used to ensure that guesses are integers
        while valid_dice_number is False:
            dice_number = get_dice_number(self)
            try:
                # checks if guess is valid
                int(dice_number)
                self.guess_dice_number = int(dice_number)
                valid_dice_number = True
            except ValueError:
                # if int(guess) fails, guess is not a number.
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
        # to be implemented
        pass

    def make_game_move(self,game,game_round,players):
        """This functions is used to get a decision of a real player.
        Options are to show dices (should remain secret), to make a valid guess,
        or to doubt the previous player and call bullshit.
        If bullshit is called the game round is finished and the looser looses a dice.
        """
        valid_decision = False
        previous_player = game_round.get_previous_player(self.player_id)
        while valid_decision is False:
            # this is used to ignore wrongly pressed keys.
            decision = input('Press s to show dices, b to call Bullshit, or g to make a Guess. ')
            if decision == 's':
                # interface object is initialized and used to show dices.
                interface = Interface()
                interface.show_dices(self)
            if decision == 'g':
                # guess is made
                self.get_guess()  
                valid_decision = True
            if decision == 'b':
                # bullshit is called and checked. This terminates the round.
                bullshit = game.check_bullshit(players,players[previous_player])
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
                    print('Correct! Do not trust your friends, it was bullshit.')
                    # previous player looses dice because of wrong guess
                    players[previous_player].dices.popitem()
                    if len(players[previous_player].dices) == 0:
                        # if it was last dice player is out of the gmae
                        players[previous_player].participates = False
                        game.active_players -= 1
                        print('That was the last dice of '+players[previous_player].name+'. You are out!')
                    return previous_player
                valid_decision = True

class Round:
        def __init__(self):
            """This class controls the status of a round and keeps
            track of player order.
            """
            self.moves = 0
            self.running = None
            self.player_order = []

        def get_previous_player(self,current_player):
            # gets previous player used to check guess and substract dice
            return self.player_order[self.player_order.index(current_player)-1]

        def get_next_player(self,current_player):
            # is used to get starter of next round if looser is out of the game
            if self.player_order.index(current_player) == len(self.player_order) -1:
                    return self.player_order[0]
            else:
                return self.player_order[self.player_order.index(current_player)+1]