from numpy.random import randint

def five_million_dice():
    return randint(low=1, high=7, size=3000000)
