import random
maara = int(input("Anna arpakuutioiden määrä: "))
summa = 0
for i in range(maara):
    summa = summa + random.randint(1, 6)
print(f"Arpakuutioiden summa: {summa}")