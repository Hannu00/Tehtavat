class Hissi:
    hissi_laskin = 1

    def __init__(self, alin, ylin, kerros_n=1):
        self.alin = alin
        self.ylin = ylin
        self.kerros_n = kerros_n
        self.kerros_u = None
        self.hissi_nro = Hissi.hissi_laskin
        Hissi.hissi_laskin += 1

    def kerros_ylos(self, ):  # Lisää kerros_n +1 eli siirtyy kerroksen ylöspäin
        self.kerros_n += 1

    def kerros_alas(self, ):  # Lisää kerros_n -1 eli siirtyy kerroksen alaspäin
        self.kerros_n -= 1

    def siirry_kerrokseen(self,
                          kerros_u):  # kerros_u on kerros johon halutaan mennä. funktio kutsuu kerros_alas tai ylos niin monta kertaa että kerros kerros_n == kerros_u
        self.kerros_u = kerros_u
        while True:
            if self.kerros_n == self.kerros_u:
                print(self.kerros_n)
                break
            elif self.kerros_n > self.kerros_u:
                print(self.kerros_n)
                self.kerros_alas()
            elif self.kerros_n < self.kerros_u:
                print(self.kerros_n)
                self.kerros_ylos()


class Talo:
    def __init__(self, a, y, h_lkm):
        self.a = a
        self.y = y
        self.h_lkm = h_lkm
        self.hissit = []
        self.luonti()

    def luonti(self):
        for i in range(self.h_lkm):
            hissi = Hissi(self.a, self.y)
            self.hissit.append(hissi)

    def aja_hissia(self, hissi_nro, kohde_k):
        hissi = self.hissit[hissi_nro]
        hissi.siirry_kerrokseen(kohde_k)

    def palo(self):
        for i in self.hissit:
            if i.kerros_n != 1:
                i.siirry_kerrokseen(1)


def hissien_sijainnit(hissit):
    for hissi in hissit:
        print(f"Hissi {hissi.hissi_nro} on kerroksessa {hissi.kerros_n}")


a_s = int(input("Hissien alin kerros?: "))
y_s = int(input("Hissien ylin kerros?: "))
h_lkm_s = int(input("Hissien lukumäärä?: "))
talo1 = Talo(a_s, y_s, h_lkm_s)

h_nro = int(input("Hissin numero mitä haluat liikuttaa?: "))
kerros = int(input("Mihin kerrokseen haluat hissin siirtyvän?: "))
talo1.aja_hissia(h_nro, kerros)

talo1.palo()
hissien_sijainnit(talo1.hissit)
