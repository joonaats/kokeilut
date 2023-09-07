gallona = float(input("Anna gallonat: "))


def litroiksi(gal):
    litra = gal * 3.875
    return litra


while gallona > 0:
    print(f"{litroiksi(gallona)} litraa")
    gallona = float(input("Anna gallonat: "))
