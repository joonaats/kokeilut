vuosi = int(input("Anna vuosi: "))
if vuosi % 100 == 0:
    if vuosi % 400 == 0:
        print("Vuosi on karkausvuosi.")
    else:
        print("Vuosi ei ole karkausvuosi.")
elif vuosi % 4 == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")