import random


def noppa():
    luku = random.randint(1, 6)
    print(luku)
    return luku


luku1 = 0
while luku1 != 6:
    luku1 = noppa()