import mysql.connector
from geopy import distance
maa = input("Anna ensimmäisen lentokennän ICAO-koodi: ")
maa2 = input("Anna toisen lentokennän ICAO-koodi: ")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='6423',
         autocommit=True
         )

def haeMatka(maa, maa2):
    sql = "SELECT latitude_deg,longitude_deg FROM airport"
    sql += " WHERE ident='" + maa + "' OR ident='" + maa2 + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(f"{distance.distance(tulos[0], tulos[1]).km:.2f} km")
    return

haeMatka(maa, maa2)

