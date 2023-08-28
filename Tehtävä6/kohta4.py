arvo = input("Syötä kokonais luku. Paina Enter lopettaaksesi: ")
lista1 = []

def laskuri(lista, koko):
    if (koko == 0):
        return 0
    else:
        return lista[koko - 1] + laskuri(lista, koko - 1)

while arvo != "":
    luku = int(arvo)
    lista1.append(luku)
    arvo = input("Syötä kokonais luku. Paina Enter lopettaaksesi: ")

tulos = laskuri(lista1, len(lista1))

print(tulos)