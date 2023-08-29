

def vihrea(teksti): print("\033[92m {}\033[00m" .format(teksti))



def punainen(teksti): print("\033[91m {}\033[00m" .format(teksti))


def kirjoita(uusi):
    with open(r"lentokentat.txt", "a") as fd:
        fd.write(f"\n{uusi}")
        print(vihrea("Tieto lisätty"))


def etsi_t(icao):
    with open(r"lentokentat.txt", "r") as fp:
        for rivi_n, rivi in enumerate(fp):
            if icao in rivi:
                return rivi


while True:
    syote = input(f'Kirjoita "lisaa" jos haluat lisätä tietoa, "etsi" jos haluat etsiä tietoa tai paina "Enter" lopettaaksesi: ')
    if syote == "":
        print("lopetetaan")
        break
    if syote == "lisaa":
        lisaa_s = input('''Kirjoita tiedot jotka haluat lisätä muodossa: "icao","iata","name","city","subd","country","elevation","lat","lon","tz","lid"\n''')
        kirjoita(lisaa_s)
    if syote == "etsi":
        etsi_s = input("Syötä lentokentän ICAO koodi etsiäksesi tietoa kentästä: ")
        print(etsi_t(etsi_s))
    else:
        print(punainen("Virheellinen syöte"))
