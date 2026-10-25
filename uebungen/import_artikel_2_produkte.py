""" Importer um neue Artikel aus txt oder csv Dateien zu importieren """

import oracledb
verbindung = oracledb.connect(
                              user="Lernen",
                              password=input("Gib dein Kennwort ein: "),
                              dsn="localhost:1521/FREEPDB1")
cursor = verbindung.cursor()
# Datei lesen und zeilenweise verarbeiten.
with open("bestellungen.txt", "r", encoding="utf-8") as datei:
    for zeile in datei:
        spalten = zeile.strip().split(",")

        # Datentypen umwandeln: ID -> int, Preis -> float
        #prod_id = int(spalten[0])
        prod_description = spalten[1]
        prod_preis = float(spalten[2])
        prod_kategorie = "Elektronik"

        # SQL Script in Variable eintragen
        tsql = "INSERT INTO PRODUKTE (NAME, PREIS_NETTO, KATEGORIE) " \
               "VALUES (:1, :2, :3)"
        #cursor.execute(tsql, prod_description,prod_preis,prod_kategorie)   <- Das geht so nicht. cursor.execute(Param1, Param2) nur zwei Parameter erlaubt
        cursor.execute(tsql, (prod_description,prod_preis,prod_kategorie)) # <- Hier wurde ein Tupel mit den () gebildet. Das klappt.

# Änderungen/Insert wegschreiben
verbindung.commit()
print("Alle Produkte sind in die Datenbank geschrieben worden.")

# Schließen
cursor.close()
verbindung.close()
