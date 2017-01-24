from __future__ import division #fixes binary division

class FlipPredictor(object):

    def __init__(self, coins):
        self.coins = coins # set of coins in bag as a list
        n = len(coins)
        self.probs=[1/n]*n # probability of a coin being the coin sel
        # begins as 1/n at first since all have equal probability

    def pheads(self):
        """
        Returns the probability of the coin returning heads on the
        next flip."""
        Heads_Normalizer = 0
        i = 0

        for coin in self.coins:
            Heads_Normalizer += self.probs[i] * coin
            i += 1

        return Heads_Normalizer

    def update(self, result):
        """
        Receives an H or T, and updates self.probs so Pheads can
        Return the correct value in future
        NOTE: All we will modify is self.probs, which contains
        joints"""
        Start_Normalizer = self.pheads()

        for i in range(0, len(self.probs)):
            if result == 'H':
                self.probs[i] = (self.coins[i] * self.probs[i]) \
                                / Start_Normalizer
            elif result == 'T':
                self.probs[i] = ((1 - self.coins[i]) * self.probs[i]) \
                                / (1 - Start_Normalizer)

# More Compact version using list comprehensions

# from __future__ import division
# class FlipPredictor(object):
#     def __init__(self,coins):
#         self.coins=coins
#         n=len(coins)
#         self.probs=[1/n]*n
#     def pheads(self):
#         return sum(pcoin*p for pcoin,p in zip(self.coins,self.probs))
#
#     def update(self,result):
#         pheads=self.pheads()
#         if result=='H':
#             self.probs=[pcoin*p/pheads for pcoin,p in zip(self.coins,self.probs)]
#         else:
#             self.probs=[(1-pcoin)*p/(1-pheads) for pcoin,p in zip(self.coins,self.probs)]
