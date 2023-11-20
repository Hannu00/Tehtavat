import random
def noppa():
   return random.randint(1,6)

luku = int()
while luku != 6:
    luku = noppa()
    print(luku)
