nimet = set()

while True:
    nimi = str(input("Syötä nimi. paina Enter lopettaaksesi: "))
    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")

    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("Seuraavat nimet syötetty")
for nimi in nimet:
    print(nimi)
