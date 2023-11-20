luku = int((input("Syötä luku. Lopuksi paina Enter: ")))
pienin = suurin = luku
int(pienin)
int(suurin)

while True:
    if luku >suurin:
        suurin = luku
    elif luku < pienin:
        pienin = luku
    elif luku == "":
        False
    luku = int((input("Syötä luku. Lopuksi paina Enter: ")))

print("Pienin syöttämäsi luku: " + pienin + "\nSuurin syöttämäsi luku: " + suurin)


