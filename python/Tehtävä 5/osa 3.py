luku = int(input("Anna luku: "))
check = 0
for i in range(1, luku):
    if luku % i == 0 and i != 1 and i != luku:
        check = 1
if check == 1:
    print(f"{luku} ei ole alkuluku.")
else:
    print(f"{luku} on alkuluku")

