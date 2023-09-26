import mysql.connector
from tabulate import tabulate
from geopy.distance import geodesic
import os

# Yhdistetään tietokantaan
def yhdista_tietokantaan():
    return mysql.connector.connect(
        host="asd",
        user="asd",
        password="asd",
        database="asd"
    )

# Hae ICAO-koordinaatit
def hae_icao_koordinaatit(icao, conn):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao,))
    return cursor.fetchone()

# Tee lentokenttähaun
def tee_lentokenttahaku(icao, conn):
    # Hae ICAO-koordinaatit
    icao_koordinaatit = hae_icao_koordinaatit(icao, conn)

    if icao_koordinaatit:
        lahtokohta_latitude = float(icao_koordinaatit["latitude_deg"])
        lahtokohta_longitude = float(icao_koordinaatit["longitude_deg"])
        lahtokohta = (lahtokohta_latitude, lahtokohta_longitude)

        # SQL kysely etsii 3 lentokenttää lähtölentokentän läheltä
        cursor = conn.cursor(dictionary=True)
        query = (
            "SELECT a.ident, a.name, a.latitude_deg, a.longitude_deg, a.type, "
            "SQRT(POW(a.latitude_deg - %s, 2) + POW(a.longitude_deg - %s, 2)) AS etaisyys, "
            "country.name AS Maa "
            "FROM airport as a "
            "JOIN country ON a.iso_country = country.iso_country "
            "WHERE a.ident != %s "
            "GROUP BY country.name "
            "ORDER BY etaisyys "
            "LIMIT 3"  # TÄTÄ muuttamalla saadaan enemmän tuloksia = voidaan näyttää kauempana olevia
        )
        cursor.execute(query, (lahtokohta_latitude, lahtokohta_longitude, icao))

        # Haetaan ja prosessoidaan tiedot
        kaikki_lentokentat = cursor.fetchall()
        cursor.close()

        # Lasketaan etäisyys
        for lentokentta in kaikki_lentokentat:
            lentokentta_latitude = float(lentokentta["latitude_deg"])
            lentokentta_longitude = float(lentokentta["longitude_deg"])
            lentokentta_coordinates = (lentokentta_latitude, lentokentta_longitude)
            etaisyys = geodesic(lahtokohta, lentokentta_coordinates).kilometers
            lentokentta["etaisyys_km"] = etaisyys

        # Järjestetään hakutulokset etäisyyden mukaan
        kaikki_lentokentat.sort(key=lambda x: float(x["etaisyys_km"]))

        # Valitaan 3 kauimpana olevaa lentokenttää
        kauimpana_olevat_lentokentat = kaikki_lentokentat[-3:]

        # Tulostetaan tulokset tabulaten avulla, mutta ei oteta mukaan "etaisyys", "latitude_deg", ja "longitude_deg"
        headers_to_exclude = ["etaisyys", "latitude_deg", "longitude_deg"]
        filtered_kauimpana_olevat_lentokentat = [
            {key: lentokentta[key] for key in lentokentta if key not in headers_to_exclude}
            for lentokentta in kauimpana_olevat_lentokentat
        ]

        headers = "keys"
        tablefmt = "fancy_grid"
        os.system("cls")
        print(tabulate(filtered_kauimpana_olevat_lentokentat, headers=headers, tablefmt=tablefmt, floatfmt=".2f"))

    else:
        os.system("cls")
        print(f"Lähtökohtaa '{icao}' ei löytynyt.")

def main():
    conn = yhdista_tietokantaan()

    while True:
        icao = input("Syötä aloitus ICAO, syötä 'q' lopettaaksesi: ")
        icao = icao.upper()

        if icao == 'Q':
            print("Lopetetaan.")
            break

        tee_lentokenttahaku(icao, conn)

    # Suljetaan tietokantayhteys
    conn.close()

if __name__ == "__main__":
    main()
