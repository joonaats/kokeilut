import requests

city = input("Anna kaupunki: ")

lampotila = 0
saatila = 0
celsius = 0

api_key = 'bfe5668c3a3915170a335598a5bbc38e'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
vastaus = requests.get(url)
if vastaus.status_code == 200:
    data = vastaus.json()
    lampotila = data['main']['temp']
    saatila = data['weather'][0]['main']
    celsius = lampotila - 273.15


elif vastaus.status_code == 404:
    print("Syötettyä kaupunkia ei löytynyt")

print(f"Kaupungin sää: {city}")
print(f"Lämpötila: {celsius:.1f} C")
print(f'Säätila: {saatila}')