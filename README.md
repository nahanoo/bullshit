# bullshit

**Bullshit the Dice game**

This is a little COVID-19 quarantine project of mine. It's kinda useless but it acted as practice for clean object orientated python programming.  
Bullshit is a funny dice game that I like to play with my mates. Unfortunately many dices are necessary, with this little module you can play the game by passing around the laptop.  
It's a mixture of console input/output and a very basic dice visualization.
Maybe one day I will make a front end or port it as a server application so you can play it by logging in with your smartphone.

Right now I have only implemented a multiplayer that you can play with your friends. I will write a bot for it in the near future.

## Installation

After cloning the repository you can install it with `pip install .`. You will be able to play the game from any directory.


## How to play

There is no fancy parser as by now so you need to create the game with a function call. You need to pass the main function how many players play the game with how many dices per player.
```
from bullshit import multiplayer as m
m.main(4,2) # this will create a game wit 4 players with 2 dices per player
```

## Rules

One player has to start and make a guess how many dices of a dice number are present in the entire round.
The dice number one is a joker and counts as any dice number.  
For example the beginner would say, that he estimates that there are three fours in the entire round.
Remember that the dice number one counts as four as well.  
The next player has to increase either the dice number or the dice count.  
So one possible game move of the next player would be that he guesses three fives or sixes. Another possible game move would be to guess that there are four dices with the dice number of choice (e.g four twos).  
You can also increase by more than one.
Another option for a valid game move is to call bullshit. You can call bullshit when you think that the guess of the previous player is wrong. If you are correct and the guess was bullshit, the previous player looses a dice. If the guess of the previous player was correct, you loose a dice. If you don't have any dices anymore, you are out! The player who lost the dice, starts the next round. If it was his last dice and he is out, the next player starts. This logic was not particularly hard to implement but not easy to code pretty. 
