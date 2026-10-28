""" Lektion 23 - Schritt 1: Text aus einer PDF-Datei auslesen """

# Notwendige Erweiterung "pypdf" nachinstalliert
# python3 -m pip install pypdf
#
# Update installiert
# pip3 install --upgrade pip
#
# Befehle:
# from pypdf import PdfReader
# reader = PdfReader("B949807855_RG.pdf")
# reader.pages() <- Liste aller Seiten
# len(reader.pages) <- Anzahl der Seiten ermitteln
# reader.pages[0] <- Zugriff auf eine Seite
# .extract_text() <- Ausgabe des Texts der angegebenen Seite
#
# Hinweise zum Umgang mit Verzeichnissen. 
# bei der Angeabe des Pfades darauf achten. Es beginnt mit \ 


from pypdf import PdfReader

PFAD =  "/Users/axelhoernschemeyer/Downloads/Oracle-Projekte/" \
        "Mobilfunkvertragsauswertung/"
DATEI = "B949807855_RG.pdf"

reader = PdfReader(PFAD+DATEI)
anzahlseiten = len(reader.pages)
seite_1_text = reader.pages[0].extract_text().split("\n")

for index, zeile in enumerate(seite_1_text):
    if "Kunden Nr." in zeile:
        kunden_nr = seite_1_text[index + 1].strip()
    elif "Datum" in zeile:
        rg_datum = seite_1_text[index + 1].strip()
    elif "Rufnummer" in zeile:
        rufnummer = seite_1_text[index + 1].strip()
    elif "Tarif" in zeile:
        tarif = seite_1_text[index + 1].strip()
    elif "Rechnung" == zeile:
        rg_nr = seite_1_text[index + 1].strip()
    elif "USt-Satz" in zeile:
        steuer = seite_1_text[index + 1].split(" ")[0]
    elif "in Höhe von" in zeile:
    # 1. Rechten Teil nach "in Höhe von " greifen
        rechter_teil = zeile.split("in Höhe von ")[1]
    # 2. Am ersten Leerzeichen trennen und das erste Wort (Index 0) nehmen
        betrag = rechter_teil.split(" ")[0]
print(f"Kundennummer {kunden_nr} - Datum {rg_datum} - Rufnummer {rufnummer} - Tarif {tarif} - Rech.-Nr. {rg_nr} - Betrag {betrag} - Steuer {steuer}")    
