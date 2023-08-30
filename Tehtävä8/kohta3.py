import mysql.connector
from geopy import distance


def haelentokenttaicao(icao):
    sql = "SELECT latitude_deg,longitude_deg FROM airport"
    sql += " WHERE ident='" + icao + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    print(tulos)
    return tulos


yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="python",
    password="salasana",
    autocommit=True
    )

while True:
    syote1 = input("Anna lentokentän ICAO paina Enter lopettaaksesi: ")
    if syote1 == "":
        print("Lopetetaan")
        break

    syote2 = input("Anna lentokentän ICAO paina Enter lopettaaksesi: ")
    if syote2 == "":
        print("Lopetetaan")
        break

    knaatti1 = haelentokenttaicao(syote1)
    knaatti2 = haelentokenttaicao(syote2)

    etaisyys = distance.distance((knaatti1[0], knaatti1[1]), (knaatti2[0], knaatti2[1]))
    etaisyys_km = etaisyys.km
    print(f"Kenttien välinen etäisyys on: {etaisyys_km:.2f}km")
