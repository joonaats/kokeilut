class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

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


class Talo:

    def __init__(self, alin, ylin, hissit):
        self.hissit1 = [Hissi(alin,ylin) for i in range(hissit)]
        self.alin = alin
        self.ylin = ylin
        self.hissit = hissit

    def aja_hissia(self, hissinumero, kerros):
        hissi = self.hissit1[hissinumero]
        hissi.siirry_kerrokseen(kerros)

    def palohalytys(self):
        for hissi in self.hissit1:
            hissi.siirry_kerrokseen(self.alin)


h = Talo(1, 5, 5)
h.aja_hissia(0, 5)
h.aja_hissia(3, 4)
h.palohalytys()