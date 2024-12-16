'''
Coin Toss
Ask the player to choose heads or tails.
Toss a coin to determine what the coin will be, and then tell the player if they were correct.
'''

import random, os, math

coin = random.randint(0,1)

if coin == 0:
    face = "Heads"
else:
    face = "Tails"

guess = (input('Heads or Tails? '))

if guess in face:
    print('You got it!')
else:
    print('You guessed wrong.')

#done