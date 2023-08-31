# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

def nopeus_f(nopeus):
    return f"{nopeus}km/h"


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.kmh = None
        self.h = None
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

    def kulje(self, h):
        self.h = h
        self.matka = self.nopeus * h



auto1 = Auto("ABC-123", "142",)

print("\nAuton rekisteritunnus: ", auto1.rekisteritunnus)
print("Auton huippunopeus: ", nopeus_f(auto1.huippunopeus))
print("Auton nopeus: ", nopeus_f(auto1.nopeus))
print("Auton kuljettu matka: ", auto1.matka)

auto1.kiihdyta(30)
auto1.kiihdyta(70)

print("\nAuton nopeus: ", nopeus_f(auto1.nopeus))

auto1.kulje(1.5)

print(f"Auton kulkema matka ajassa 1.5h: {auto1.matka}km")




