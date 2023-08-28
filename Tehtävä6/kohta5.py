import random
#luodaan ensimmäinen lista johonka käyttäjä syöttää koon
random.seed(0)
l_koko = int(input("Syötä listan koko: "))
k = [random.randint(1, 999) for i in range(l_koko)]
#luodaan toinen lista nimelät k2
k2 = []
#funktio joka lisää alkuperäisen listan numeroista parilliset uuteen listaan
def karsija(lista, lista2):
    for i in range(len(lista)):
        vali = int(lista[i])
        if vali % 2 == 0:
            lista2.append(vali)
    return
#kutsutaan funktio
karsija(k,k2)
#tulostetaan molemmat listat
print(f"{k}\n{k2}")
