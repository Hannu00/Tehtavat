import math

pizza_h1 = float(input("Syötä pizzan1 halkaisija senttimetreinä: "))
pizza_e1 = float(input("Syötä pizzan1 hinta euroina: "))

pizza_h2 = float(input("Syötä pizzan2 halkaisija senttimetreinä: "))
pizza_e2 = float(input("Syötä pizzan2 hinta euroina: "))

def pizzuri(halkaisija,eurot):
    a = math.pi * (halkaisija / 2) ** 2
    b = a / eurot
    return b

pizza1 = pizzuri(pizza_h1,pizza_e1)
pizza2 = pizzuri(pizza_h2,pizza_e2)

if pizza1 > pizza2:
    print(f"Pizza1 on parempi kuin pizza2")
else:
    print(f"Pizza2 on parempi kuin pizza1")
