import math

# luoti 13.3g naula 425.6g leiviskä 8512g
leiviska = int(input("Anna leiviskät: "))
naula = int(input("Anna naulat: "))
luoti = int(input("Anna luodit: "))

leiviskat = 8512 * leiviska
naulat = 425.6 * naula
luodit = 13.3 * luoti

grammat = (leiviskat + naulat + luodit)

kilot = grammat / 1000
kilot = math.floor(kilot)
kilot = kilot * 1000
grammat = grammat - kilot
kilot = kilot / 1000

print(f"Massa nyky mittojen mukaan: {kilot} kilogrammaa  ja {grammat:.2f} grammaa.")
