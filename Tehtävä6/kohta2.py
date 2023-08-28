import random

tahko = int(input("Syötä tahkojen määrä: "))
def noppa():
   return random.randint(1,tahko)

luku = int()
while luku != tahko:
    luku = noppa()
    print(luku)
