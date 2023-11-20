

def vihrea(teksti):                             # Tämän avulla voidaan muokata tekstin väriä
    return "\033[92m {}\033[00m" .format(teksti)


def punainen(teksti):                             # Tämän avulla voidaan muokata tekstin väriä
    return "\033[91m {}\033[00m" .format(teksti)


def kirjoita(uusi):                                 # Kun tiedostoon halutaan lisätä uuden kentän tiedot käytetään kirjoita funktiota
    with open(r"lentokentat.txt", "a") as fd:
        fd.write(f"\n{uusi}")
        print(vihrea("Tieto lisätty"))


def etsi_t(icao):                                   # Etsii ICAO koodin perusteella tiedostosta löytyvän lentokentän ja tulostaa sen tiedot
    with open("lentokentat.txt", "r", encoding="utf-8") as fp:
        for rivi_n, rivi in enumerate(fp):
            if icao in rivi:
                return rivi
        return punainen("Ei löytynyt")


syote = "asd"

while syote != "":
    syote = input(f'Kirjoita "lisaa" jos haluat lisätä tietoa, "etsi" jos haluat etsiä tietoa tai paina "Enter" lopettaaksesi: ')
    if syote == "":                                 #Kun käyttäjä painaa enter kun kysytään mitä halutaan tehdä loop sulkeutuu. Tämän voisi myös vaihtaa komentoon "lopeta" "" sijaan.
        print(punainen("lopetetaan"))
        break
    elif syote == "lisaa":                          #Jos halutaan lisätä uuden kentän tietoja kysytään tiedot yksitellen käyttäjältä. (Tämän vois varmaankin siistiä jotenkin)
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
        if lisaa_IATA in etsi_t(lisaa_IATA):
            print(punainen(lisaa_ICAO), "tiedot on jo syötetty.\n", etsi_t(lisaa_ICAO))
        else:
                lisaa_l = [lisaa_ICAO, lisaa_IATA, lisaa_NAME, lisaa_CITY, lisaa_SUBD, lisaa_COUNTRY, lisaa_ELEVATION, lisaa_LAT, lisaa_LON, lisaa_TZ, lisaa_LID]
                kirjoita(lisaa_l)
    elif syote == "etsi":                           #Jos käyttäjä syöttää etsi komennon....
        etsi_s = input("Syötä lentokentän ICAO koodi etsiäksesi tietoa kentästä: ")
        print(etsi_t(etsi_s))
    else:                                           #Jos komentoa ei tunnisteta annetaan siitä virheilmoitus punaisella tekstillä
        print(punainen("Virheellinen syöte"))
