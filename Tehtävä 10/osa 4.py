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

class Kilpailu:

    def __init__(self, nimi, kilometrit, autolista):
        self.nimi = nimi
        self.kilometrit = kilometrit
        self.autolista = autolista

    def tunti_kuluu(self):
        tunti = 0
        while not self.kilpailu_ohi():
            for x in autot:
                x.kiihdyta(r.randint(-10, 15))
                x.kulje(1)
            tunti += 1
            if tunti % 10 == 0:
                self.tulosta_tilanne()

    def tulosta_tilanne(self):
        for t in self.autolista:
            print(f"{t.rekisteri} {t.hnopeus} {t.nopeus} {t.matka}")

    def kilpailu_ohi(self):
        for b in self.autolista:
            if b.matka > self.kilometrit:
                self.tulosta_tilanne()
                return True
        return False


autot = []
for i in range(10):
    auto = Auto(f"ABC-{i + 1}", r.randint(100, 200))
    autot.append(auto)
k = Kilpailu("Suuri romuralli", 8000, autot)
k.tunti_kuluu()
