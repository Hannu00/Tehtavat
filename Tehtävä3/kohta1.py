kuha = float(input("Syötä kuhan pituus senttimetreinä: "))
mitta = float(37)
tulos = mitta - kuha

if kuha<mitta:
    print("Laske kuha takaisin!\n",f"Alimmasta sallitusta pyyntimitasta puuttuu: {tulos:.2f}cm")
else:
    print("Hieno saalis!")