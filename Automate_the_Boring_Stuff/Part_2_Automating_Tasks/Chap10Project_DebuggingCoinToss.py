#! python3

import random

guess = ''

while guess not in ('heads','tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
tossNum = random.randint(0,1)  #0 is tails, 1 is heads
if tossNum == 1:
    toss = 'heads'
elif tossNum == 0:
    toss = 'tails'
if toss == guess:
    print('You got it right!')
else:
    print('Nope! Guess again.')
    guess = input()
    if toss == guess:
        print('You got it right!')
    else:
        print('Nope. You are really bad at this game...')
