'''
Number Guessing Game
Have the computer generate a random number from 1 to 100.  
The players will try to guess the number, and the computer will tell them if they are too high or too low.  
Play continues until they guess correctly at which point the computer tells them how many guesses it took.
'''

import math, random, os

number = random.randint(1,100)

guess = 0

guesscount = 0

while guess != number:
    guess = int(input('Guess a number from 1-100: '))
    if guess > 100 or guess < 1:
        print('Guess must be within 1-100')
    else:
        if guess < number:
            print('Your guess was too low')
        if guess > number:
            print('Your guess was too high')
    guesscount += 1

print(f'You guessed it! It took {guesscount} guesses.')

#done