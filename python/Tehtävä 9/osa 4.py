import random as r


class Auto:
    def __init__(self, rekisteri, hnopeus, nopeus="0", matka="0"):
        self.rekisteri = rekisteri
        self.hnopeus = int(hnopeus)
        self.nopeus = int(nopeus)
        self.matka = float(matka)

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.hnopeus:
            self.nopeus = self.hnopeus

    def kulje(self, tunnit):
        self.matka += (self.nopeus * tunnit)


testi = 1
autot2 = []
for i in range(10):
    auto = Auto(f"ABC-{testi}", r.randint(100, 200))
    testi += 1
    autot2.append(auto)
check = True
while check:
    for x in autot2:
        x.kiihdyta(r.randint(-10, 15))
        x.kulje(1)
        if x.matka > 10000:
            check = False
for z in autot2:
    print(f"{z.rekisteri} {z.hnopeus} {z.nopeus} {z.matka}")
