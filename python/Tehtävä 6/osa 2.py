import random
tahko = int(input("Anna nopan tahkojen määrä: "))


def noppa(tahko1):
    luku = random.randint(1, tahko1)
    print(luku)
    return luku


luku1 = 0
while luku1 != tahko:
    luku1 = noppa(tahko)
