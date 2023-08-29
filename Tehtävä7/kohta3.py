

def vihrea(teksti):
    return "\033[92m {}\033[00m" .format(teksti)


def punainen(teksti):
    return "\033[91m {}\033[00m" .format(teksti)


def kirjoita(uusi):
    with open(r"lentokentat.txt", "a") as fd:
        fd.write(f"\n{uusi}")
        print(vihrea("Tieto lisätty"))


def etsi_t(icao):
    with open("lentokentat.txt", "r", encoding="utf-8") as fp:
        for rivi_n, rivi in enumerate(fp):
            if icao in rivi:
                return rivi
        return punainen("Ei löytynyt")


while True:
    syote = input(f'Kirjoita "lisaa" jos haluat lisätä tietoa, "etsi" jos haluat etsiä tietoa tai paina "Enter" lopettaaksesi: ')
    if syote == "":
        print(punainen("lopetetaan"))
        break
    elif syote == "lisaa":
        lisaa_ICAO = input("Kentän ICAO: ")
        lisaa_IATA = input("Kentän IATA: ")
        lisaa_NAME = input("Kentän NAME: ")
        lisaa_CITY = input("Kentän CITY: ")
        lisaa_SUBD = input("Kentän SUBD: ")
        lisaa_COUNTRY = input("Kentän COUNTRY: ")
        lisaa_ELEVATION = input("Kentän ELEVATION: ")
        lisaa_LAT = input("Kentän LAT: ")
        lisaa_LON = input("Kentän LON: ")
        lisaa_TZ = input("Kentän TZ: ")
        lisaa_LID = input("Kentän LID: ")
        lisaa_l = [lisaa_ICAO, lisaa_IATA, lisaa_NAME, lisaa_CITY, lisaa_SUBD, lisaa_COUNTRY, lisaa_ELEVATION, lisaa_LAT, lisaa_LON, lisaa_TZ, lisaa_LID]
        kirjoita(lisaa_l)
    elif syote == "etsi":
        etsi_s = input("Syötä lentokentän ICAO koodi etsiäksesi tietoa kentästä: ")
        print(etsi_t(etsi_s))
    else:
        print(punainen("Virheellinen syöte"))
