lentoasemat = dict()
valinta = ""
while valinta != "l":
    valinta = input("Valitse: (s)yötä uusi lentoasema, (h)ae lentoasema, (l)opeta: ")

    if valinta == "s":
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[koodi] = nimi

    if valinta == "h":
        koodi = input("Annaa lentoaseman ICAO-koodi: ")
        print(lentoasemat[koodi])
