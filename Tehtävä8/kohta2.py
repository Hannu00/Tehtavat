import mysql.connector
from tabulate import tabulate

def haelentokenttaicao(maakoodi):
    sql = "SELECT type, count(*) FROM airport"
    sql += " WHERE iso_country='" + maakoodi + "'"
    sql += " GROUP BY type"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tabulate(tulos, tablefmt="fancy_grid"))
    return


yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
    )

while True:
    maakoodi = input("Anna maakoodi. paina Enter lopettaaksesi: ")
    if maakoodi == "":
        print("Lopetetaan")
        break
    else:
        haelentokenttaicao(maakoodi)