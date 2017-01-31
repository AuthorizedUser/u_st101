from random import randint, shuffle

N = 1000

def simulate(N):
    K = 0 #count how often you succeed in variable k

    for i in range(0, N):
        doorlist = [1, 2, 3]
        shuffle(doorlist)
        cardoor = randint(1, 3)
        choice = randint(1, 3)

        for door in doorlist:
            if door != cardoor and door != choice:
                montychoice = door

        for door in doorlist:
            if door != montychoice and door != choice:
                switchchoice = door

        if cardoor == switchchoice:
            K += 1

    return float(K) / float(N)

print simulate(1000)
