def listapari(lista):
    uusilista = []
    for i in lista:
        if i % 2 == 0:
            uusilista.append(i)
    return uusilista


lista1 = [5, 9, 30, 999, -100]
print(lista1)
print(listapari(lista1))
