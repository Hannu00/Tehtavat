sukupuoli = input("Syötä sukupuolesi: ")
hemo = int(input("Syötä hemoglobiiniarvosi (g/l): "))

if sukupuoli=="mies":
    if 117<=hemo<=175:
        print("Normaali.")
    elif hemo<=117:
        print("Alhainen.")
    elif 175<=hemo:
        print("Korkea.")

elif sukupuoli=="nainen":
    if 134<=hemo<=195:
        print("Normaali.")
    elif hemo<=134:
        print("Alhainen.")
    elif 195<=hemo:
        print("Korkea.")
else:
    print("Tarkista sukupuoli syötteesi!")



