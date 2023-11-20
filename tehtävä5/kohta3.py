Alkuluku = "Tosi"
a = int(input("Syötä luku: "))
for i in range(2, a):
    if a % i == 0:
        Alkuluku = "Epätosi"
        break
print(str(a), "on alkuluku:", str(Alkuluku))
