import random

MIN = 1
MAX = 6


def function():
    again = 'y'

    while again == 'y' or again == 'Y':
        print('Rolling dice...')
        print('Their values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        again = input(print('Would you like to roll again? (y = yes)'))


function()
