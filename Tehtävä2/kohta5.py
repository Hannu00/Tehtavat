leiviska = float(input("Syötä leiviskät: "))
naula = float(input("Syötä naulat: "))
luoti = float(input("Syötä luodit: "))

naula = naula + (leiviska * 20)
luoti = luoti + (naula * 32)
paino = float(luoti * 13.3)
kilo = int(paino / 1000)
gramma = paino % 1000
grammaval = round(gramma, 2)

print("Massa nykymittojen mukaan:")
print(str(kilo) + "kg", "ja", str(grammaval) + "grammaa")
