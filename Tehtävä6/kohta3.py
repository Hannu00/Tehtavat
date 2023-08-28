
syote = int(input("Syötä gallonat: "))
def muunnin(gal):
   return gal * 3.785

luku = int()
while syote > 0:
    luku = muunnin(syote)
    print(f"{luku:.2f}")
    syote = int(input("Syötä gallonat: "))