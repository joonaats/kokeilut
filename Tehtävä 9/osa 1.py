class Auto:
    def __init__(self, rekisteri, hnopeus, nopeus="0", matka="0"):
        self.rekisteri = rekisteri
        self.hnopeus = hnopeus
        self.nopeus = nopeus
        self.matka = matka


auto1 = Auto("ABC-123", 142)
print(f"{auto1.rekisteri} {auto1.hnopeus} {auto1.nopeus} {auto1.matka}")
