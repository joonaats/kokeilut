def listasumma(lista):
    summa = 0
    for i in lista:
        summa = summa + i
    return summa


lista1 = [5, 9, 30, 999, -100]
print(listasumma(lista1))