import requests

def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    vastaus = requests.get(url)

    if vastaus.status_code == 200:
        vitsi_tiedot = vastaus.json()
        return vitsi_tiedot['value']
    else:
        return "Vitsin hakeminen epäonnistui."

def main():
    print("Tässä on satunnainen Chuck Norris -vitsi:")
    chuck_norris_vitsi = hae_chuck_norris_vitsi()
    print(chuck_norris_vitsi)

if __name__ == "__main__":
    main()
