lista = []
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    lista.append(float(luku))
lista.sort(reverse=True)
for i in range(5):
    print(lista[i])
