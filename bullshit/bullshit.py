import random

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
            players[player_id] = Player(player_id,n_dices_per_player)
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
    def __init__(self,name,n_dices_per_player):
        
        # Player is still in round
        self.participates = True

        # Name of a player and dices of a person
        self.name = name
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

class Round:
        def __init__(self):
            self.running = None
            self.player_order = []
