vuosi = int(input("Syötä vuosi: "))
epa = str("Vuosi ei ole karkausvuosi.")
tosi = str("Vuosi on karkausvuosi.")

if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print(tosi)
        else:
            print(epa)
    else:
        print(tosi)
else:
    print(epa)
