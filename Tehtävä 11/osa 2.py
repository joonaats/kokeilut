import random as r


class Auto:
    def __init__(self, rekisteri, hnopeus, nopeus=0, matka="0"):
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


class Sahkoauto(Auto):

    def __init__(self, rekisteri, hnopeus, nopeus, akku, matka=0):
        super().__init__(rekisteri, hnopeus, nopeus, matka)
        self.akku = akku


class Polttomoottoriauto(Auto):

    def __init__(self, rekisteri, hnopeus, nopeus, bensa, matka=0):
        super().__init__(rekisteri, hnopeus, nopeus, matka)
        self.bensa = bensa

autot = []
autot.append(Sahkoauto("ABC-15", 180, 60, 52.5))
autot.append(Polttomoottoriauto("ACD-123", 165, 50, 32.3))
for i in autot:
    i.kulje(3)
    print(f"{i.rekisteri} {i.hnopeus} {i.nopeus} {i.matka}")