hytti = input("Syötä hyttiluokkasi: ")

LUX_hytti = "LUX on parvekkeellinen hytti yläkannella."
A_hytti = "A on ikkunallinen hytti autokannen yläpuolella."
B_hytti = "B on ikkunaton hytti autokannen yläpuolella."
C_hytti = "C on ikkunaton hytti autokannen alapuolella."

if hytti=="LUX":
    print(LUX_hytti)
elif hytti=="A":
    print(A_hytti)
elif hytti=="B":
    print(B_hytti)
elif hytti=="C":
    print(C_hytti)
else:
    print("Tarkista syötteesi!")
