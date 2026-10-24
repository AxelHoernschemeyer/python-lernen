# Lektion 18 - Zeilenweise lesen & Text-Parsing (CSV-Prinzip)
#
# Zwei wichtige Hilfsmittel für Textzeilen
#   .strip():       Entfernt unsichtbare Steuerzeichen und Zeilenumbrüche (\n) am Anfang und Ende
#   .split(","):    Zerschneidet eine Zeile an den Kommas und liefert eine Liste mit den Einzelwerten zurück!
#
# Beispiel:     with open("kunden.txt", "w", encoding="utf-8") as datei:
#                   datei.write("K101,Müller,500\nK102,Weber,1200")
#
#               with open("kunden.txt", "r", encoding="utf-8") as datei:
#                   for zeile in datei:
#                       spalten = zeile.strip().split(",") # ["K101", "Müller", "500"]
#                       print(f"Kunde: {spalten[1]} | Umsatz: {spalten[2]} €")
#
# Aufgabe:  Erstelle im w-Modus eine Datei "bestellungen.txt" mit folgendem Inhalt:
#           "101,Tastatur,49.99\n102,Maus,19.99\n103,Monitor,199.99"
#
#           Öffne die Datei im r-Modus, gehe mit einer for-Schleife Zeile für Zeile durch,
#           zerlege jede Zeile mit .strip() und .split(",") und gib für jedes Produkt folgenden Satz aus
#           "Artikel: Tastatur - Preis: 49.99 €"

with open("bestellungen.txt", "w", encoding="utf-8") as datei:
    datei.write("101,Tastatur,49.99\n102,Maus,19.99\n103,Monitor,199.99")

with open("bestellungen.txt", "r", encoding="utf-8") as datei:
    for zeile in datei:
        spalten = zeile.strip().split(",")
        print(f"Artikel: {spalten[1]} - Preis: {spalten[2]} €")