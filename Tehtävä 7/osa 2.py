nimet = set()
nimi = "b"

while nimi != '':
    nimi = input("Anna nimi: ")
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    elif nimi != '':
        print("Uusi nimi")
        nimet.add(nimi)

for i in nimet:
    print(i)
