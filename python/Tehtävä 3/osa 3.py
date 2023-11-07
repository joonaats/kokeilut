sukupuoli = input("Anna sukupuoli: ")
hemo = int(input("Anna hemoglobiiniarvo: "))
if sukupuoli == "nainen":
    if hemo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemo >= 117 & hemo <= 175:
        print("Hemoglobiiniarvo on normaali")
    else:
        print("Hemoglobiiniarvo on korkea")
elif sukupuoli == "mies":
    if hemo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemo >= 134 & hemo <= 195:
        print("Hemoglobiiniarvo on normaali")
    else:
        print("Hemoglobiiniarvo on korkea")