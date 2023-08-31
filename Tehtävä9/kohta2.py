# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

def nopeus_f(nopeus):
    return f"{nopeus}km/h"


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.kmh = None
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self, kmh):
        self.kmh = kmh
        self.nopeus = self.nopeus + self.kmh
        if self.nopeus > 142:
            self.nopeus = 142
        elif self.nopeus < 0:
            self.nopeus = 0


auto1 = Auto("ABC-123", "142",)

print("\nAuton rekisteritunnus: ", auto1.rekisteritunnus)
print("Auton huippunopeus: ", nopeus_f(auto1.huippunopeus))
print("Auton nopeus: ", nopeus_f(auto1.nopeus))
print("Auton kuljettu matka: ", auto1.matka)

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print("\nAuton nopeus: ", nopeus_f(auto1.nopeus))

auto1.kiihdyta(-200)

print("Auton nopeus: ", nopeus_f(auto1.nopeus))