from flask import Flask, jsonify

app = Flask(__name__)

def on_alkuluku(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:numero>', methods=['GET'])
def tarkista_alkuluku(numero):
    on_alkuluku_bool = on_alkuluku(numero)
    vastaus = {
        "Number": numero,
        "isPrime": on_alkuluku_bool
    }
    return jsonify(vastaus)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
