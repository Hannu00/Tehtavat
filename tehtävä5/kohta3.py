Alkuluku = True
a = int(input("Syötä luku: "))
for i in range (2,a):
    if a % i == 0:
        Alkuluku = False
        break
print(str(a),"on alkuluku:",str(Alkuluku))
