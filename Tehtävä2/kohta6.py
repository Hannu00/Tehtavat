import random

# Kolmi numeroinen koodi. Luodaan tekemällä kaksi eri numeroa jotka yhdistetään jotta koodin ensimmäinen numero voi olla myös 0
yksi = str(random.randint(0,9))
kaksi = str(random.randint(10,99))
kolme = yksi+kaksi

# Neli numeroinen koodi
nelja = random.randint(1000,6666)

# Tulostetaan koodit
print(yksi+kaksi)
print(nelja)