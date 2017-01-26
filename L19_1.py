#Write a function flip that simulates flipping n fair coins.
#It should return a list representing the result of each flip as a 1 or 0
#To generate randomness, you can use the function random.random() to get
#a number between 0 or 1. Checking if it's less than 0.5 can help your
#transform it to be 0 or 1

from random import random as r
from math import sqrt

def mean(data):
    return float(sum(data))/len(data)

def variance(data):
    mu=mean(data)
    return sum([(x-mu)**2 for x in data])/len(data)

def stddev(data):
    return sqrt(variance(data))


def flip(N):
    """Returns a list representing 0 or 1 as results of N coin flips"""

    # flip_list = []
    # for i in range(0, N):
    #     if r() < 0.5:
    #         flip = 1
    #     else:
    #         flip = 0
    #     flip_list.append(flip)
    # return flip_list

    return [(lambda x: 1 if r() < 0.5 else 0)(x) for x in range(0, N)]
# Use lambda list comprehension to be compact

N=1000
f=flip(N)

print mean(f)
print stddev(f)
