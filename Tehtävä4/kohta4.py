import random

Vastaus = random.randint(1, 10+1)
Arvaus = int(input("Arvaa luku 1-10\n"))

while Arvaus != Vastaus:
    if Arvaus > Vastaus:
        print("Liian suuri arvaus")
    elif Arvaus < Vastaus:
        print("Liian pieni arvaus")
        Arvaus = int(input("Arvaa luku 1-10\n"))
print("Oikein")

