import mysql.connector


def haelentokenttaicao(maakoodi):
    sql = "SELECT type as 'Kentän tyyppi',count(*) as 'lkm' FROM airport"
    sql += " WHERE iso_country='" + maakoodi + "'"
    sql += " GROUP BY type"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
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
    maakoodi = input("Anna maakoodi. paina Enter lopettaaksesi: ")
    if maakoodi == "":
        print("Lopetetaan")
        break
    else:
        haelentokenttaicao(maakoodi)