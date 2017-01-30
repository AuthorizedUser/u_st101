#Write
from math import sqrt
from __future__ import division

def mean(l):
    return float(sum(l))/len(l)

def var(l):
    m = mean(l)
    return sum([(x-m)**2 for x in l])/len(l)

def factor(l):
    return 1.96


def conf(l):
    """Takes a set of data and computes the confidence interval"""
    return factor(l) * sqrt(var(l)/len(l))

def test(l, h):

    upperci = mean(l) + conf(l)
    lowerci = mean(l) - conf(l)

    if h <= upperci and h >= lowerci:
        return True
    else:
        return False
