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


auto1 = Auto("ABC-123", 142)
print(f"{auto1.rekisteri} {auto1.hnopeus} {auto1.nopeus} {auto1.matka}")
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"{auto1.nopeus}")
auto1.kiihdyta(-200)
print(f"{auto1.nopeus}")
