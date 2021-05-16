import random

class Bullshit:
    """Bullshti dice game engine"""
    def __init__(self):
        self.running = None
        self.players = dict()

   
    class Player:
        """A player which has dices, an guess and some helper functions"""
        def __init__(self,name,n_dices_per_player):
            class Guess:
                """Guess of a player about dice numbers and dice counts of a rond"""
                def __init__(self):
                    self.dice_number = None
                    self.dice_count = None

            class Dice:
                def __init__(self):
                    self.dice_number = None
            
            # Player is still in round
            self.participates = None

            # Name of a player and dices of a person
            self.name = name
            self.n_dices_per_player = n_dices_per_player

            # Create dices of a player
            self.dices = dict()
            for n in range(self.n_dices_per_player):
                self.dices[n] = Dice()

            # Create guess object
            self.guess = Guess()

        def roll_dices(self):
            """Roll the dices of a player"""
            for dice in self.dices.values():
                dice.dice_number = random.randint(1,6)

        def print_throw(self):
            """Print the throw of a player"""
            dices = [str(v.dice_number) for v in list(self.dices.values())]
            print(''.join(['|','|'.join(dices),'|']))

        def set_guess(self,dice_number,dice_count):
            """Set guess of a player"""
            self.guess.dice_number = int(dice_number)
            self.guess.dice_count = int(dice_count)

    
    class Round():
        def __init__(self):
            self.round = self.Players

    def create_players(self,n_players,n_dices_per_player):
        """Create muliplte players with n dices per player"""
        for n in range(n_players):
            name = 'player_'+str(n)
            self.players[name] = self.Player(name,n_dices_per_player)


    def check_bullshit(self,players,guesser):
        """Check if estimate of a player is bullshit"""
        dice_count = 0
        for player in players.values():
            for dice in player.dices.values():
                if dice.dice_number == guesser.guess.dice_number or dice.dice_number == 1:
                    dice_count += 1
        if dice_count >= guesser.guess.dice_count:
            return False
        else:
            return True


