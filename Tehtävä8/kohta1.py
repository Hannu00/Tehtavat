import mysql.connector
from tabulate import tabulate


def haelentokenttaicao(icao_koodi):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + icao_koodi + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            print(tabulate(tulos,headers=["Lentokentän nimi", "Kunta"], tablefmt="fancy_grid"))
    return


yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user=input("Syötä käyttäjätunnus: "),
    password=input("Syötä salasana: "),
    autocommit=True
    )
icao = 0

while icao != "":
    icao = input("Anna lentokentän ICAO paina Enter lopettaaksesi: ")
    if icao == "":
        print("Lopetetaan")
    else:
        haelentokenttaicao(icao)