luvut = []
luku = input("Syötä luku ja lopuksi paina Enter lopettaaksesi: ")

while luku != "":
        x = int(luku)
        luvut.append(x)
        luku = input("Syötä luku ja lopuksi paina Enter lopettaaksesi: ")

luvut.sort(reverse=True)
if len(luvut) >= 5:
    for i in range(5):
        print(luvut[i])
else:
    print("Listassa ei tarpeeksi numeroita!")
