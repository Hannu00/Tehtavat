hytti = input("Syötä hyttiluokkasi: ")

LUX_hytti = "LUX on parvekkeellinen hytti yläkannella."
A_hytti = "A on ikkunallinen hytti autokannen yläpuolella."
B_hytti = "B on ikkunaton hytti autokannen yläpuolella."
C_hytti = "C on ikkunaton hytti autokannen alapuolella."

if hytti=="LUX" or hytti=="lux" or hytti=="Lux":
    print(LUX_hytti)
elif hytti=="A" or hytti=="a":
    print(A_hytti)
elif hytti=="B" or hytti=="b":
    print(B_hytti)
elif hytti=="C" or hytti=="c":
    print(C_hytti)
else:
    print("Tarkista syötteesi!")
