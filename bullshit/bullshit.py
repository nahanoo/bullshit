import random

class Bullshit:
    """Bullshti dice game engine"""
    def __init__(self):
        self.running = False
        self.players = dict()
        self.game_round = None
        self.active_players = 0
        self.bot = False
   
    class Player:
        """A player which has dices, an guess and some helper functions"""
        class Guess:
                """Guess of a player about dice numbers and dice counts of a round"""
                def __init__(self):
                    self.dice_number = None
                    self.dice_count = None

        class Dice:
            def __init__(self):
                self.dice_number = None
        def __init__(self,name,n_dices_per_player):
            
            # Player is still in round
            self.participates = True

            # Name of a player and dices of a person
            self.name = name
            self.n_dices_per_player = n_dices_per_player

            # Create dices of a player
            self.dices = dict()
            for n in range(self.n_dices_per_player):
                self.dices[n] = self.Dice()

            # Create guess object
            self.guess = self.Guess()

        def roll_dices(self):
            """Roll the dices of a player"""
            for dice in self.dices.values():
                dice.dice_number = random.randint(1,6)

        def print_throw(self):
            """Print the throw of a player"""
            dices = [str(v.dice_number) for v in list(self.dices.values())]
            print(''.join(['|','|'.join(dices),'|']))

    
    class Round():
        def __init__(self):
            self.running = None
            self.player_order = []

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

    def change_player_order(self,looser):
        names = list(self.players.keys())
        reordered_names = []
        looser_index = names.index(looser)
        for i in range(looser_index,len(names)):
            reordered_names.append(names[i])
        for i in range(looser_index):
            reordered_names.append(names[i])
        previous_player_order = self.players
        self.players = dict()
        for name in reordered_names:
            self.players[name] = previous_player_order[name]
