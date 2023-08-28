salasana = "rules"
kayttajatunnus = "python"
kayttaja_s = str(input("Syötä käyttäjätunnus: "))
salasana_s = str(input("Syötä salasana: "))

while salasana_s != salasana and kayttaja_s != kayttajatunnus:
    print("Pääsy evätty")
    kayttaja_s = str(input("Syötä käyttäjätunnus: "))
    salasana_s = str(input("Syötä salasana: "))

print("Tervetuloa!")