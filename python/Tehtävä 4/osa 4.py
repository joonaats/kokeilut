import random
oikea = random.randint(1, 10)
while True:
    vastaus = int(input("Anna luku: "))
    if vastaus > oikea:
        print("Liian suuri vastaus")
    if vastaus < oikea:
        print("Liian pieni vastaus")
    if vastaus == oikea:
        print("Oikein")
        break

