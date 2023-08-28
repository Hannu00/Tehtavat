import random

random.seed(0)
l_koko = int(input("Syötä listan koko"))
k = [random.randint(1, 999) for i in range(l_koko)]

k2 = []


def karsija(k):
    for i in range(l_koko):
        if k[i] % 2 == 0:
            print("just")
        else:
            k2.append(k[i])


print(k, "\n", k2)
