
from __future__ import division

def mean(oldmean, n, x):
    newcount = n + 1
    aggregate = (n * oldmean) + x
    return aggregate / newcount
