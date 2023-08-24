vuosi = int(input("Syötä vuosi: "))

if vuosi % 4 == 0:
    print("Vuosi on karkausvuosi.")
elif vuosi % 100 == 0 and vuosi % 400 == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")
