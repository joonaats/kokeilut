import mysql.connector

maa = input("Anna lentokennän maakoodi (esim. FI): ")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='6423',
         autocommit=True
         )

def haeMaara(maa):
    sql = "SELECT COUNT(type),type FROM airport"
    sql += " WHERE iso_country='" + maa + "'"
    sql += " GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            print(f"{rivi}")
    return

haeMaara(maa)

