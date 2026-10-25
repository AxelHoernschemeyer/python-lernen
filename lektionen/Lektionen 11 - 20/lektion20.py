""" Einleitung und Beschreibung """
# Lektion 20 - Das Finale: Oracle Datenbankanbindung (oracledb)
#
# Das Grundprinzip einer Datenbankverbindung in Python:
#   1.  Verbindung herstellen (connect): 
#           Benutzername
#           Passwort
#           Host
#           Port
#           Service-Name
#
#   2.  Cursor erstellen (cursor): Der cursor ist dein "Werkzeug" zum ausführen von SQL-Befehlen
#
#   3.  SQL ausführen (execute): Z.B. SELECT oder INSERT
#
#   4.  Änderungen speichern (commit): Bei schreibenden Zugriffen (INSERT, UPDATE).
#
#   5.  Schließen (close): Verbindung sauber trennen.
#
# Syntax-Beispiel:
#   import oracledb
#
#   - Verbindung zum Oracle Docker-Container herstellen
#       verbindung = oracledb.connect(
#                                   user="system",
#                                   password="dein_passwort",
#                                   dsn="localhost:1521/FREEPDB1"  # Host:Port/ServiceName
#                                    )
#
#     cursor = verbindung.cursor()
#
#    - SQL-Befehl ausführen
#       cursor.execute("SELECT 'Hallo Oracle' FROM dual")
#       ergebnis = cursor.fetchone()
#       print(ergebnis[0])
#
#    - Ressourcen wieder schließen
#        cursor.close()
#        verbindung.close()

import oracledb
kennwort = input("Gib dein Kennwort ein: ")
tsql = "Select * from Bundesliga_tipps Where Spieltag = 7"
verbindung = oracledb.connect(
                                user="lernen",
                                password=kennwort,
                                dsn="localhost:1521/FREEPDB1"
                            )
cursor = verbindung.cursor()
#cursor.execute("Select SYSDATE from DUAL")
cursor.execute(tsql)
ergebnis = cursor.fetchone()
print(ergebnis)

cursor.close()
verbindung.close()