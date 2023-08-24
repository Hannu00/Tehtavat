luvut = []
luku = (input("Syötä luku. Lopuksi paina Enter: "))

while luku!="":
    luvut.append(luku)
    luku = input("Syötä luku. Lopuksi paina Enter: ")

print("Pienin syöttämäsi luku: " + min(luvut) + "\nSuurin syöttämäsi luku: " + max(luvut))


