# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="lentopeli"
)

cursor = mydb.cursor(dictionary=True)

@app.route('/kenttä/<icao>', methods=['GET'])

def haku(icao):
    cursor.execute("SELECT ident AS 'ICAO', name, municipality FROM airport WHERE ident = %s", (icao,))
    current_lentokentta = cursor.fetchone()
    current_lentokentta = jsonify(current_lentokentta)
    return current_lentokentta

if __name__ == '__main__':
    app.run(debug=True, port=3000)