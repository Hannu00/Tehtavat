import mysql.connector


def haelentokenttaicao(icao):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + icao + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(tulos)
    return


yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="python",
    password="salasana",
    autocommit=True
    )

while True:
    icao = input("Anna lentokentän ICAO paina Enter lopettaaksesi: ")
    if icao == "":
        print("Lopetetaan")
        break
else:
    haelentokenttaicao(icao)