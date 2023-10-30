# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat.
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
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

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Matka: {self.matka}")


# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
class Sahkoauto(Auto):
    def __init__(self, akku, rekisteritunnus, huippunopeus):
        self.akku = akku
        super().__init__(rekisteritunnus, huippunopeus)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()


# Polttomoottoriauton ominaisuutena on bensatankin koko litroina.

class Polttoauto(Auto):

    def __init__(self, tankki, rekisteritunnus, huippunopeus):
        self.tankki = tankki
        super().__init__(rekisteritunnus, huippunopeus)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()

# Kirjoita pääohjelma, jossa luot yhden
# sähköauton (ABC-15, 180 km/h, 52.5 kWh)
# ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus,
# käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.


auto1 = Sahkoauto(52.5, "ABC-15", 180)
auto2 = Polttoauto(32.3, "ACD-123", 165)
auto1.nopeus = 100
auto2.nopeus = 100

auto1.kulje(3)
auto2.kulje(3)

auto1.tulosta_tiedot()
auto2.tulosta_tiedot()