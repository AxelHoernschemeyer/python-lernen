""" Importer um neue Artikel aus txt oder csv Dateien zu importieren """

import oracledb
# Bereich für die Variablen
FILENAME = str("bestellungen_2.txt")

try:
    with open(FILENAME, "r", encoding="utf-8") as datei:
        # Kennwort abfrage
        PASSCODE = input("Gib dein Kennwort an: ")
        
        # Datenbankverbinung aufbauen
        verbindung = oracledb.connect(
                            user="Lernen",
                            password=PASSCODE,
                            dsn="localhost:1521/FREEPDB1")
        cursor = verbindung.cursor()

        # Datei zeilenweise einlesen und an Datenbank übergeben
        for zeile in datei:
            spalten = zeile.strip().split(",")

            # Datentypen umwandeln: ID -> int, Preis -> float
            try:
                #prod_id = int(spalten[0])
                prod_description = spalten[1]
                prod_preis = float(spalten[2])
                prod_kategorie = spalten[3].upper()

                # SQL Script in Variable eintragen
                tsql = "INSERT INTO PRODUKTE (NAME, PREIS_NETTO, KATEGORIE) " \
                       "VALUES (:1, :2, :3)"
                #cursor.execute(tsql, prod_description,prod_preis,prod_kategorie)   
                # <- Das geht so nicht. cursor.execute(Param1, Param2) nur zwei Parameter erlaubt
                cursor.execute(tsql, (prod_description,prod_preis,prod_kategorie))
                # <- Hier wurde ein Tupel mit den () gebildet. Das klappt.
            except (ValueError, IndexError) as e:
                #Fehler in einer LogDatei speichern. Import Dateinamen mit einbinden.
                with open("import_fehler.log", "a", encoding="utf-8") as logfile:
                    logfile.write(f"Fehlerhafte Zeile übersprungen: {zeile.strip()} | Grund: {e}\n")
                continue                                                                       

        # Änderungen/Insert wegschreiben
        verbindung.commit()
        print("Alle Produkte sind in die Datenbank geschrieben worden.")

        # Datenbankverbindung schließen
        cursor.close()
        verbindung.close()

except FileNotFoundError:
    print(f"Datei {FILENAME} konnte nicht gefunden werden!")
except oracledb.Error as e:
    print(f"X Datenbankfehler {e}")

        

