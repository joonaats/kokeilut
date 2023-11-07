import mysql.connector

icao = input("Anna lentokennän ICAO-koodi: ")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='6423',
         autocommit=True
         )

def haeNimi(icao):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + icao + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            print(f"Lentokentän nimi: {rivi[0]}, sijaintikunta: {rivi[1]}")
    return

haeNimi(icao)

