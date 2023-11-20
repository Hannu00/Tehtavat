import mysql.connector
from tabulate import tabulate
from geopy.distance import geodesic
import os
import time

lentokone1 = '''
     __|__
--o--(_)--o--
'''
lentokone2 = '''
    __|__
 --o--(_)--o--
'''

icao = "a"
icaot_syotetty = []
# Yhdistetään tietokantaan
def yhdista_tietokantaan():
    return mysql.connector.connect(
        host="54.37.204.19",
        user="u106905_7AsIM13PeT",
        password="!.f05FLEFDQ=lu5uhjUx@Gb4",
        database="s106905_lentomopo"
    )
conn = yhdista_tietokantaan()
def siirtyminen(icao):
    os.system('cls')
    icaot_syotetty.append(icao)
    print(lentokone1)
    time.sleep(0.5)
    print(lentokone2)
    time.sleep(0.5)
    print(lentokone1)
    time.sleep(0.5)
    tee_lentokenttahaku(icao, conn)

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
            "c.name AS Maa "
            "FROM airport as a "
            "JOIN country AS c ON a.iso_country = c.iso_country "
            "WHERE a.ident != %s AND a.type != 'small_airport'"
            "GROUP BY c.name "
            "ORDER BY etaisyys "
            "LIMIT 6"  # TÄTÄ muuttamalla saadaan enemmän tuloksia = voidaan näyttää kauempana olevia
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
        pienin = min(kaikki_lentokentat, key=lambda x: x["etaisyys_km"])
        keski = kaikki_lentokentat[len(kaikki_lentokentat) // 2]
        suurin = max(kaikki_lentokentat, key=lambda x: x["etaisyys_km"])


        # Tulostetaan tulokset tabulaten avulla, mutta ei oteta mukaan "etaisyys", "latitude_deg", ja "longitude_deg"
        headers_to_exclude = ["etaisyys", "latitude_deg", "longitude_deg"]
        filtered_kauimpana_olevat_lentokentat = [
            {key: lentokentta[key] for key in lentokentta if key not in headers_to_exclude}
            for lentokentta in [pienin, suurin, keski]
        ]

        headers = "keys"
        tablefmt = "fancy_grid"
        print(tabulate(filtered_kauimpana_olevat_lentokentat, headers=headers, tablefmt=tablefmt, floatfmt=".2f"))

    else:
        print(f"Lähtökohtaa '{icao}' ei löytynyt.")

def main():
    conn = yhdista_tietokantaan()
    icao = "a"
    icaot_syotetty = []
    while icao != "Q":
        icao = input("Syötä aloitus ICAO, syötä 'q' lopettaaksesi: ")
        icao = icao.upper()

        if icao == 'Q':
            print("Lopetetaan.")
            break

        elif icao in icaot_syotetty:
            print("Olet käynyt jo syöttämälläsi lentokentällä")
            time.sleep(1)

        else:
            siirtyminen(icao)


    # Suljetaan tietokantayhteys
    conn.close()

if __name__ == "__main__":
    main()
