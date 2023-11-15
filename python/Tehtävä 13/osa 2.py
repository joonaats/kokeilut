from flask import Flask, request
import mysql.connector

app = Flask(__name__)


@app.route('/kenttä/<ICAO>')
def LentokenttienKaupungit(ICAO):



    sql = "SELECT airport.name FROM country, airport"
    sql += " WHERE country.iso_country = airport.iso_country"
    sql += " AND airport.ident = '" + ICAO + "'"

    sql2 = "SELECT municipality FROM country, airport"
    sql2 += " WHERE country.iso_country = airport.iso_country"
    sql2 += " AND airport.ident = '" + ICAO + "'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    kursori.execute(sql2)
    tulos2 = kursori.fetchall()

    nimi = str(tulos)
    nimi2 = nimi.strip("[('',)]")
    kaupunki = str(tulos2)
    city2 = kaupunki.strip("[('',)]")

    vastaus = {
        "ICAO": ICAO,
        "Name": nimi2,
        "Municipality": city2
    }
    return vastaus

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='6423',
    autocommit=True
)

if __name__ == '__main__':
    app.run(use_reloader=True, host="127.0.0.1", port=3000)