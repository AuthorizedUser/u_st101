from math import sqrt
data3=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]

def mean(data):
    return sum(data) / len(data)

def variance(data):
    mu = mean(data)
    return mean([x-mu)**2 for x in data])
#This is not my code for variance, it was copied. Mine included
# an easy-to-read but space consuming for-loop but has been
# overwritten

def stddev(data):
    return sqrt(variance(data))
#Technically exercise 6 but it's so short I put it here
