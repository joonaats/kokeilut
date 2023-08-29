attempts = 0
while True:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    attempts = attempts + 1
    if attempts >= 5:
        print("Pääsy evätty")
        break


