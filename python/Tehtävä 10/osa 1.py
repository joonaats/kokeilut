class Hissi:
    def __init__(self, alin, ylin, kerros=0):
        self.alin = alin
        self.ylin = ylin
        kerros = alin
        self.kerros = kerros

    def siirry_kerrokseen(self, kerros):
        while kerros > self.kerros and self.kerros < self.ylin:
            self.kerros_ylos()
        while kerros < self.kerros and self.kerros > self.alin:
            self.kerros_alas()

    def kerros_ylos(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Nykyinen kerros: {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Nykyinen kerros: {self.kerros}")


h = Hissi(1,5)
h.siirry_kerrokseen(8)
h.siirry_kerrokseen(-1)