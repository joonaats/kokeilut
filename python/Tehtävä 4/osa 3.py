numero = 1
index = 0
list = []
while True:
    numero = input("Anna luku: ")
    if numero == "":
        break
    list.append(int(numero))
suurin = list[0]
pienin = list[0]
for i in list:
    if i > suurin:
        suurin = i
    if i < pienin:
        pienin = i
print(f"Pienin luku on {pienin} ja suurin on {suurin}")
