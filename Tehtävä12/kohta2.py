import requests


def hae_saatiedot(api_avain, paikkakunta):
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    params = f'{paikkakunta}&appid={api_avain}'

    vastaus = requests.get(base_url + params)

    if vastaus.status_code == 200:
        sailytys = vastaus.json()
        sailytys_lampotila_kelvin = sailytys['main']['temp']
        sailytys_lampotila_celsius = kelvin_celsiukseksi(sailytys_lampotila_kelvin)
        sailytys_saatila = sailytys['weather'][0]['description']
        return f"Sää paikkakunnalla {paikkakunta}: {sailytys_saatila}, lämpötila: {sailytys_lampotila_celsius:.2f}°C"
    else:
        return "Sään hakeminen epäonnistui."


def kelvin_celsiukseksi(kelvin):
    return kelvin - 273.15


def main():
    api_avain = "1b27d0f478ffabe4ed51d4170c7f97e9"
    paikkakunta = input("Syötä paikkakunnan nimi: ")

    sailytys_tiedot = hae_saatiedot(api_avain, paikkakunta)

    print(sailytys_tiedot)


if __name__ == "__main__":
    main()
