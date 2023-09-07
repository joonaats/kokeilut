def hintalasku(halkaisija, hinta):
    alue = 3.14*((halkaisija/2)**2)
    testi = 10000/alue
    neliohinta = testi * hinta
    return neliohinta


halkaisija1 = float(input("Anna pizzan halkaisija (cm): "))
hinta1 = float(input("Anna pizzan hinta: "))
print(hintalasku(halkaisija1, hinta1))
