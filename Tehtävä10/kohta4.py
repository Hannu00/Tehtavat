from random import randint
from tabulate import tabulate


# def nopeus_f(nopeus):
# return f"{nopeus}km/h"

def lajittelu(x):
    return x[3]


class Auto:
    tehty = 0

    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.kmh = None
        self.h = None
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
        Auto.tehty = Auto.tehty + 1

    def kiihdyta(self, kmh):
        self.kmh = kmh
        self.nopeus = self.nopeus + self.kmh
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, h):
        self.h = h
        self.matka = self.matka + self.nopeus * h


class Kilpailu:
    def __init__(self, kilpailu_nimi, pituus, osallistujat):
        self.kilpailu_nimi = kilpailu_nimi
        self.pituus = pituus
        self.osallistujat = osallistujat

    def tunti_kuluu(self):
        for auto in autot:
            auto.kulje(1)
            auto.kiihdyta(randint(-10, 10))

    def tulosta_tilanne(self):
        autot_maali = []
        for auto in autot:
            autot_maali.append([auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka])

        autot_maali.sort(reverse=True, key=lajittelu)
        print(tabulate(autot_maali, headers=["Rekisteritunnus", "Huippunopeus km/h", "Nopeus km/h", "Matka km"],
                       tablefmt="fancy_grid"))

    def kilpailu_ohi(self):
        for auto in autot:
            if auto.matka >= self.pituus:
                return True
        return False


autot = []
for i in range(10):
    auto = Auto(f"ABC-{i + 1}", randint(100, 200))
    autot.append(auto)

kilpailu1 = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while not kilpailu1.kilpailu_ohi():
    if tunnit % 10 == 0 and tunnit != 0:
        kilpailu1.tulosta_tilanne()
    kilpailu1.tunti_kuluu()
    tunnit += 1

print("Kilpailu päättyi.")
print("Kilpailu kesti:", tunnit, "tuntia.")
kilpailu1.tulosta_tilanne()
