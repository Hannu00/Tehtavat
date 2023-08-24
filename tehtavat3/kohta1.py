kuha = float(input("Syötä kuhan pituus senttimetreinä: "))
mitta = float(37)

if kuha<mitta:
    print("Laske kuha takaisin!\n","Alimmasta sallitusta pyyntimitasta puuttuu: ", mitta - kuha,"cm")
else:
    print("Hieno saalis!")