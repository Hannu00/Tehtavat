from random import randint
from tabulate import tabulate


#def nopeus_f(nopeus):
    #return f"{nopeus}km/h"

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
        if self.nopeus > 142:
            self.nopeus = 142
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, h):
        self.h = h
        self.matka = self.matka + self.nopeus * h


autot = []
for i in range(10):
    auto = Auto(f"ABC-{i+1}", randint(100, 200))
    autot.append(auto)

maali = False

while not maali:
    for auto in autot:
        if auto.matka >= 10000:
            voittaja = auto.rekisteritunnus
            print(f"Kisa päättyi voittaja auton rekisteritunnus on {auto.rekisteritunnus}.")
            maali = True
            break
    if not maali:
        for auto in autot:
            auto.kulje(1)
            auto.kiihdyta(randint(-10, 10))

autot_maali = []
for auto in autot:
    autot_maali.append([auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka])

autot_maali.sort(reverse=True, key=lajittelu)

print(tabulate(autot_maali, headers=["Rekisteritunnus", "Huippunopeus", "Nopeus", "Matka"], tablefmt="fancy_grid"))
