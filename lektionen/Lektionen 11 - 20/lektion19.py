""" Einleitung """
# Lektion 19 - Fehlerbehandlung mit try / except
#
# Bevor wir Daten in eine Datenbank schreiben oder Dateien verarbeiten, müssen wir verhindern, 
# dass unser Skript abstürzt, wenn etwas schiefgeht (z. B. wenn eine Datei nicht 
# existiert oder eine Zahl unlesbar ist).
#
# Konzept:
# Mit einem try / except-Block fängst du Fehler kontrolliert ab:
#   try:
#       with open("nicht_vorhanden.txt", "r", encoding= "utf-8") as datei: 
#           inhalt = datei.read()
#   except FileNotFoundError:
#       print("! Die Datei wurde leider nicht gefunden!")
# 
# Aufgabe:
#   Versuche mit open() im "r"-Modus eine Datei namens
#   "datenbank_export.csv" zu öffnen.
#   Fange den Fehler mit except FileNotFoundError ab und gib im Fehlerfall
#   die Meldung "Fehler: Die Export-Datei ist noch nicht vorhanden!"
# 

try:
    with open("datenbank_export.csv", "r", encoding="utf-8") as datei:
        inhalt = datei.read()
except FileNotFoundError:
    print("Fehler: Die Export-Datei ist noch nicht vorhanden!")