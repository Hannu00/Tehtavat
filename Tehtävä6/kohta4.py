arvo = input("Syötä kokonais luku. Paina Enter lopettaaksesi: ")
lista1 = []


def laskuri(lista):
    return sum(lista)


while arvo != "":
    luku = int(arvo)
    lista1.append(luku)
    arvo = input("Syötä kokonais luku. Paina Enter lopettaaksesi: ")

print(laskuri(lista1))
