import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('Guess value is : ' + guess)
num = random.randint(0, 1) # 0 is tails, 1 is heads
if num == 0:
    toss = 'tails'
else:
    toss = 'heads'
logging.debug('toss value is : ' + str(toss))
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug('Guess value is : ' + guess)
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')