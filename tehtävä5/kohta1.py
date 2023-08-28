import random

noppa = random.randint(1,6)
tulokset = []
lkm = int(input("Montako noppaa heitetään? \n"))

for i in range(lkm):
    tulokset.append(noppa)
    noppa = random.randint(1, 6)
print("Noppien summa:",sum(tulokset))


