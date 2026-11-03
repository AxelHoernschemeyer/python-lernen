🐍 Python Lernjournal
Repository: python-lernen
Ziel: Python von Grund auf lernen und sicher für Automatisierungen, Datenverarbeitung & Datenbankanbindungen anwenden.

📌 Inhaltsverzeichnis

Überblick & Ziele
Lektion 01 – Variablen und Ausgaben
Lektion 02 – Datentypen
Lektion 03 – Rechnen mit Zahlen
Lektion 04 – Benutzereingaben
Lektion 05 – Datentypen umwandeln
Lektion 06 – Bedingungen mit if
Lektion 07 – Bedingungen mit elif & logische Operatoren
📝 Zwischenprüfung 01
Lektion 08 – Schleifen mit while
Lektion 09 – for-Schleifen
Lektion 10 – Listen
Lektion 11 – Schleifen mit Listen
Lektion 12 – Listenfunktionen & Berechnungen
Lektion 13 – Verschachtelte Schleifen
🛠️ Praxisübung 01 – Wochen-Wetterbericht
Lektion 14 – Eigene Funktionen (def)
Lektion 15 – Parameter & Standardwerte
Lektion 16 – Mehrere Rückgabewerte & Variable Unpacking
Lektion 17 – Dateizugriffe (open())
Lektion 18 – Zeilenweises Lesen & Text-Parsing
Lektion 19 – Fehlerbehandlung (try / except)
Lektion 20 – Oracle-Datenbankanbindung (oracledb)
🛠️ Praxisübung 02 – Datei-Import in Oracle-Datenbank
Lektion 21 – Fehler-Logging & Robuster CSV-Import
Lektion 22 – DB-Schema- & Datenanalyse sowie PDF-Strukturzuordnung
Lektion 23 – PDF-Parsing mit pypdf, Anker-Prinzip & Text-Extraction
Lektion 24 – Modulare Architektur & Rechnungs-Parsing (pdf_utils, get_vendor, get_invoice_details, main)
Lektion 25 – Oracle-Import (RECHNUNGS_KOPF), DB-IDs, Dynamic Exceptions & shutil-Archivierung
📊 Zusammenfassung & Aktueller Lernstand
🎯 Nächste Meilensteine
Überblick & Ziele

🚀 Langfristige Schwerpunkte

Python-Grundlagen (Variablen, Bedingungen, Schleifen, Listen)
Datentypen & Datenstrukturen
Funktionen, Module & Dateiverarbeitung (open(), read(), write())
Fehlerbehandlung (try / except)
Objektorientierte Programmierung (OOP)
Automatisierung, PDF-Auswertungen & Datenbankanbindungen (Oracle)
🛠️ Praxisprojekte

PDF-Rechnungen automatisiert auswerten
Daten validieren & Fehler protokollieren
Datenbanken anbinden & Importprozesse steuern
Lektion 01 – Variablen und Ausgaben

📚 Gelernt

Variablen anlegen und Werte zuweisen
Texte und Zahlen mit print() ausgeben
Variablen in Ausgaben kombinieren
💻 Übungen

Persönliche Daten in Variablen gespeichert
Eigene Textausgaben mit print() erstellt
💡 Erkenntnisse

✅ In Python müssen Variablen nicht explizit deklariert werden.
✅ Python erkennt den Datentyp automatisch anhand des zugewiesenen Wertes.
✅ Mehrere Werte können per Komma getrennt in print() ausgeben werden.

🎯 Status

✅ Verstanden

Lektion 02 – Datentypen

📚 Gelernt

Datentyp	Beschreibung	Beispiel
str	Text (String)	"Axel"
int	Ganze Zahl (Integer)	54
float	Gleitkommazahl (Float)	1.82
bool	Wahrheitswert (Boolean)	True / False
💻 Übungen

Variablen mit verschiedenen Datentypen angelegt
Datentypen mit type() überprüft
💡 Erkenntnisse

✅ Python unterscheidet strikt zwischen Text und Zahlen.
✅ Identisch aussehende Inhalte können unterschiedliche Datentypen besitzen:

54 $\rightarrow$ int
"54" $\rightarrow$ str
1.82 $\rightarrow$ float
True $\rightarrow$ bool
🎯 Status

✅ Verstanden

Lektion 03 – Rechnen mit Zahlen

📚 Gelernt

Grundrechenarten: Addition (+), Subtraktion (-), Multiplikation (*), Division (/)
Ganzzahldivision (//)
Modulo (%)
💻 Übungen

Rechnen mit Variablen
Restwertbestimmung mit Modulo
Ganzzahlige Ergebnisse ohne Nachkommastellen berechnen
💡 Erkenntnisse

✅ Modulo (%) liefert den Rest einer Division (z. B. 20 % 3 $\rightarrow$ 2).
✅ Ganzzahldivision (//) schneidet Nachkommastellen ab (z. B. 20 // 3 $\rightarrow$ 6).
✅ Strings können mit Integer multipliziert werden (z. B. "Axel" * 3 $\rightarrow$ "AxelAxelAxel").
✅ Addition von String und Integer führt zu einem TypeError (z. B. "5" + 1).

🎯 Status

✅ Verstanden

Lektion 04 – Benutzereingaben

📚 Gelernt

Interaktive Benutzereingaben mit input()
Verarbeitung und Ausgabe von Eingaben
💻 Übungen

Vorname, Alter und Wohnort über die Konsole abgefragt
Eingaben personalisiert ausgegeben
💡 Erkenntnisse

✅ input() liefert immer einen String (str) zurück – selbst wenn der Benutzer eine Zahl eingibt.
✅ Zahlen aus input() müssen vor mathematischen Rechnungen umgewandelt werden.

🎯 Status

✅ Verstanden

Lektion 05 – Datentypen umwandeln

📚 Gelernt

Typumwandlung mit int() und float()
Unterscheidung zwischen int() und round()
💻 Übungen

Benutzereingaben in Zahlen umgewandelt und mathematisch berechnet
Verhalten bei Nachkommastellen getestet
💡 Erkenntnisse

✅ int() wandelt Strings in Ganzzahlen um und schneidet Nachkommastellen ab (int(54.9) $\rightarrow$ 54).
✅ round() rundet kaufmännisch (round(54.9) $\rightarrow$ 55).
✅ Nur Strings, die reine Ziffern enthalten, können mit int() umgewandelt werden (andernfalls ValueError).

🎯 Status

✅ Verstanden

Lektion 06 – Bedingungen mit if

📚 Gelernt

Vergleichsoperatoren (<, <=, >, >=, ==, !=)
Verzweigungen mit if und else
💻 Übungen

Prüfen von Volljährigkeit und Minderjährigkeit
💡 Erkenntnisse

✅ Bedingungen ergeben immer den Wahrheitswert True oder False.
✅ = ist die Wertzuweisung, == ist der Wertvergleich.
✅ Mit else wird der Alternativzweig ausgeführt, wenn die if-Bedingung nicht zutrifft.

🎯 Status

✅ Verstanden

Lektion 07 – Bedingungen mit elif & logische Operatoren

📚 Gelernt

Mehrfachverzweigungen mit elif
Logische Operatoren and und or
💻 Übungen

Auswertung von Schulnoten
Zuordnung von Altersgruppen
Kombination mehrerer Bedingungen in einer Abfrage
💡 Erkenntnisse

✅ Python arbeitet if / elif / else von oben nach unten ab und führt nur den ersten zutreffenden Zweig aus.
✅ and: Beide Bedingungen müssen wahr sein.
✅ or: Mindestens eine Bedingung muss wahr sein.

🎯 Status

✅ Verstanden

📝 Zwischenprüfung 01

📚 Geprüfte Themen

Variablen, Datentypen, Rechenoperatoren, Benutzereingaben, Typumwandlung, Verzweigungen (if/elif/else), Vergleichsoperatoren, and, or.

🏆 Ergebnis

9 von 10 Punkten

💡 Erkenntnisse

✅ Grundlegende Syntax und Logik sicher beherrscht.
⚠️ Wichtiger Merksatz für die Zukunft: Aufgabenstellungen genau und vollständig lesen.

🎯 Status

✅ Bestanden

Lektion 08 – Schleifen mit while

📚 Gelernt

Bedingungsgesteuerte Schleifen mit while
Zählvariablen und Kurzschreibweisen (+= 1, -= 1)
Vermeidung von Endlosschleifen
Kombination von Schleifen und if-Bedingungen
💻 Übungen

Vorwärts- und Rückwärtszählen
Berechnung von Quadratzahlen
Unterscheidung gerader und ungerader Zahlen
Dynamische Schleifendurchläufe mit Benutzereingabe
💡 Erkenntnisse

✅ while-Schleifen laufen, solange die Bedingung True bleibt.
✅ Die Zählvariable muss innerhalb der Schleife angepasst werden, um Endlosschleifen zu vermeiden.

🎯 Status

✅ Verstanden

Lektion 09 – for-Schleifen

📚 Gelernt

Anzahlgesteuerte Schleifen mit for
Zahlenbereiche erzeugen mit range(start, ende, schrittweite)
Rückwärts zählen mit negativer Schrittweite
💻 Übungen

Zahlenreihen ausgeben (1 bis 10)
Gerade Zahlen mit Schrittweite 2 ausgeben
Rückwärts zählen (10 bis 1)
💡 Erkenntnisse

✅ Ideal, wenn die Anzahl der Durchläufe im Voraus bekannt ist.
✅ Bei range(start, ende) ist der Endwert exklusiv (wird nicht erreicht).

🎯 Status

✅ Verstanden

Lektion 10 – Listen

📚 Gelernt

Erstellen von Listen (liste = [...])
Lese- und Schreibzugriff über Indizes (beginnend bei 0)
Neue Elemente mit .append() hinzufügen
Listenlänge bestimmen mit len()
Zugriff vom Ende mit negativen Indizes (-1, -2)
💻 Übungen

Städteliste angelegt und gepflegt
Elemente geändert und erweitert
Letztes Element per negativem Index ermittelt
💡 Erkenntnisse

✅ Indizes starten bei 0.
✅ liste[-1] greift direkt auf das letzte Element zu.
✅ Nicht existierende Indizes lösen einen IndexError: list index out of range aus.

🎯 Status

✅ Verstanden

Lektion 11 – Schleifen mit Listen

📚 Gelernt

Iterieren über Listen mit for element in liste:
Filtern von Listenwerten mit Bedingungen (if) innerhalb der Schleife
Zugehörigkeitsprüfung mit in (z. B. if note in [1, 2]:)
💻 Übungen

Filterung guter Noten (1 und 2) aus einer gegebenen Notenliste und formatierte Ausgabe.
💡 Erkenntnisse

✅ Schleifen greifen nacheinander auf jedes Element einer Liste zu.
✅ Kombination aus for und if ermöglicht das gezielte Auswählen von Werten.

🎯 Status

✅ Verstanden

Lektion 12 – Listenfunktionen & Berechnungen

📚 Gelernt

Eingebaute Funktionen für numerische Listen: len(), sum(), min(), max()
Berechnung von Statistiken (z. B. Notendurchschnitt: summe / anzahl)
Kaufmännisches und ganzzahliges Runden von Ergebnissen mit round()
💻 Übungen

Erfassung einer Notenliste, Ermittlung der Gesamtanzahl (len), Notensumme (sum) und Berechnung des gerundeten Notendurchschnitts.
💡 Erkenntnisse

✅ sum(liste) berechnet die Gesamtsumme aller Zahlen in einer Liste.
✅ len(liste) gibt die Elementanzahl zurück.
✅ Der Durchschnitt lässt sich direkt über sum(liste) / len(liste) ermitteln.

🎯 Status

✅ Verstanden

Lektion 13 – Verschachtelte Schleifen

📚 Gelernt

Konzept ineinander verschachtelter Schleifen (Nested Loops)
Innere Schleife wird bei jedem Durchlauf der äußeren Schleife vollständig ausgeführt
Kombination mehrerer Listen zur Erzeugung von Kreuzprodukten / Paarungen
💻 Übungen

Kombination zweier Listen (vornamen und nachnamen) zur Ausgabe aller Namenskombinationen.
💡 Erkenntnisse

✅ Für jedes Element der äußeren Schleife wird die innere Schleife komplett durchlaufen.
✅ Wenn die äußere Liste $N$ Elemente und die innere Liste $M$ Elemente hat, gibt es insgesamt $N \times M$ Durchläufe.

🎯 Status

✅ Verstanden

🛠️ Praxisübung 01 – Wochen-Wetterbericht

📚 Gelernt & Angewendet

Praktische Kombination aus for-Schleifen, Akkumulatoren (summe += temp), verketteten Vergleichsoperatoren (20 <= temp <= 25) und if/elif/else
Berechnung und Rundung von Durchschnittswerten über Listen (round(summe / len(temperaturen), 1))
💻 Code-Lösung

temperaturen = [18, 22, 15, 25, 30, 12, 27]
summe = 0

for temp in temperaturen:
    summe += temp
    if 20 <= temp <= 25:
        print("Angenehmer Tag:", temp, "°C")
    elif temp < 20:
        print("Kühler Tag:", temp, "°C")
    else:
        print("Heißer Tag:", temp, "°C")

print("Durchschnitt der Woche:", round(summe / len(temperaturen), 1), "°C")
💡 Erkenntnisse

✅ Python erlaubt elegante verkettete Vergleiche wie 20 <= temp <= 25.
✅ Kombination aus Schleifen, Verzweigungen und mathematischen Funktionen festigt das Verständnis für reale Datenverarbeitungsprozesse.

🎯 Status

✅ Erfolgreich gelöst

Lektion 14 – Eigene Funktionen (def)

📚 Gelernt

Funktionen definieren mit def funktion_name(parameter):
Codeblöcke wiederverwendbar kapseln (DRY-Prinzip: Don't Repeat Yourself)
Ergebnisse mit return zurückgeben
Dokumentation über Docstrings (""" ... """)
Beheben von Pylint-Warnungen (missing-function-docstring)
💻 Übungen

Funktion berechne_quadratzahl(zahl) geschrieben, die das Quadrat berechnet und per return zurückgibt.
Funktion mit Parameter 5 aufgerufen und Ergebnis ausgegeben (25).
💡 Erkenntnisse

✅ def leitet die Funktionsdefinition ein.
✅ return beendet die Funktion und gibt den berechneten Wert an den Aufrufer zurück.
✅ Klammern um den Rückgabewert bei return sind optional (Konvention in Python: return ergebnis ohne Klammern).

🎯 Status

✅ Verstanden

Lektion 15 – Parameter & Standardwerte

📚 Gelernt

Übergabe mehrerer Parameter an Funktionen
Festlegen von Standardwerten (Default Values) bei der Funktionsdefinition (z. B. mwst_satz=19)
Überschreiben von Standardwerten beim Aufruf durch explizite Argumente
💻 Übungen

Erstellung der Funktion berechne_preis(netto, mwst_satz=19) zur Bruttoberechnung mit optional abweichendem Steuersatz.
💡 Erkenntnisse

✅ Wird ein Argument beim Aufruf weggelassen, greift automatisch der definierte Standardwert.
✅ Werden alle Parameter beim Aufruf angegeben, wird der Standardwert für diesen Durchlauf überschrieben.

🎯 Status

✅ Verstanden

Lektion 16 – Mehrere Rückgabewerte & Variable Unpacking

📚 Gelernt

Rückgabe mehrerer kommagetrennter Werte aus einer Funktion (return wert1, wert2, wert3)
Direktes Entpacken der Rückgabewerte in mehrere Variablen beim Aufruf (Variable Unpacking: a, b, c = funktion())
Vermeidung doppelter Berechnungen durch Zwischenvariablen innerhalb von Funktionen
💻 Übungen

Funktion berechne_statistik(zahlen_liste) zur Ermittlung von Summe, Anzahl und gerundetem Durchschnitt aus einer Zahlenliste.
💡 Erkenntnisse

✅ Kommagetrennte return-Werte werden von Python als Tupel zurückgegeben und lassen sich beim Aufruf direkt entpacken.
✅ Verwendung von lokalen Variablen (gesamtsumme, anzahl) erhöht Lesbarkeit und Performance.

🎯 Status

✅ Verstanden

Lektion 17 – Dateizugriffe (open())

📚 Gelernt

Öffnen und Schließen von Dateien mit dem with open(...) as datei:-Block (automatisches Schließen/Ressourcenverwaltung)
Modi: "w" (schreiben/überschreiben), "a" (anhängen), "r" (lesen)
Zeichenkodierung mit encoding="utf-8" für plattformübergreifende Umlautsicherheit
Schreiben mit .write() und Auslesen des gesamten Inhalts mit .read()
💻 Übungen

Schreiben von zwei Logzeilen in "log.txt" im "w"-Modus und Auslesen des Inhalts im "r"-Modus.
💡 Erkenntnisse

✅ with open() stellt sicher, dass Dateien selbst bei Fehlern im Code sauber geschlossen werden.
✅ encoding="utf-8" verhindert Umlaut-Fehler beim Wechsel zwischen Mac und Windows.

🎯 Status

✅ Verstanden

Lektion 18 – Zeilenweises Lesen & Text-Parsing

📚 Gelernt

Zeilenweises Iterieren über Dateien (for zeile in datei:) für speichereffiziente Verarbeitung großer Datenmengen
Entfernen von unsichtbaren Steuerzeichen & Zeilenumbrüchen (\n) mit .strip()
Zerschneiden von strukturierten Textzeilen (CSV-Prinzip) mit .split(",") in Listen
Gezielter Zugriff auf Spalten über Indizes (spalten[0], spalten[1], etc.)
Elegante Formatierung von Strings mit f-Strings (f"Artikel: {spalten[1]} - Preis: {spalten[2]} €")
💻 Übungen

Erstellung einer Bestellungsdatei "bestellungen.txt", zeilenweises Einlesen, Zerlegen der Felder mit .strip().split(",") und formatierte Ausgabe im Terminal.
💡 Erkenntnisse

✅ Zeilenweises Lesen verbraucht kaum Arbeitsspeicher und eignet sich perfekt für große CSV-Dateien und spätere Datenbank-Imports.
✅ Kombination aus .strip() und .split(",") zerlegt Rohdaten direkt in sauber verarbeitbare Spalten-Listen.

🎯 Status

✅ Verstanden

Lektion 19 – Fehlerbehandlung (try / except)

📚 Gelernt

Abfangen von Laufzeitfehlern (Exceptions) mit try / except
Gezieltes Abfangen spezifischer Fehler wie FileNotFoundError oder ValueError
Verhindern von unkontrollierten Programmabstürzen bei fehlenden Dateien oder ungültigen Eingaben
💻 Übungen

Erstellung einer Fehlerabfrage mit try:, um das Fehlen einer CSV-Export-Datei sauber abzufangen und eine verständliche Fehlermeldung auszugeben.
💡 Erkenntnisse

✅ try: umschließt den potenziell fehleranfälligen Codeabschnitt.
✅ except FileNotFoundError: wird nur ausgeführt, wenn genau dieser Fehler auftritt.
✅ Robuste Fehlerbehandlung ist essenziell für automatisierte Import-Skripte und Datenbankprozesse.

🎯 Status

✅ Verstanden

Lektion 20 – Oracle-Datenbankanbindung (oracledb)

📚 Gelernt

Installation von externen Python-Bibliotheken im Terminal über python3 -m pip install oracledb
Importieren der Bibliotheken ganz oben im Skript (import oracledb)
Verbindungsaufbau zur lokalen Oracle-Datenbank im Docker-Container (oracledb.connect(user, password, dsn))
Arbeiten mit dem Cursor (verbindung.cursor()) zum Ausführen von SQL-Abfragen (cursor.execute())
Ergebnisabfrage mit cursor.fetchone() und formatiertes Ausgeben mit f-Strings
Sauberes Schließen von Cursor (cursor.close()) und Verbindung (verbindung.close())
💻 Übungen

Ausführen einer SQL-Abfrage (SELECT SYSDATE FROM DUAL) auf der lokalen Oracle-Datenbank und formatierte Ausgabe des Systemdatums.
💡 Erkenntnisse

✅ import oracledb muss zwingend vor der ersten Nutzung aufgerufen werden.
✅ cursor.fetchone() liefert ein Ergebnis-Tupel zurück.
✅ Das Schließen von Cursorn und Verbindungen gibt Ressourcen auf dem Datenbankserver wieder frei.

🎯 Status

✅ Verstanden

🛠️ Praxisübung 02 – Datei-Import in Oracle-Datenbank

📚 Gelernt & Angewendet

Kombination aus Datei-Parsing (open(), .strip().split(",")) und Oracle-Datenbankimport (oracledb)
Übergabe dynamischer Werte an SQL INSERT mit Bind-Variablen (:1, :2, :3) als Parameter-Tupel
Transaktionssteuerung mit verbindung.commit() und sauberes Schließen von Cursor und Verbindung
💻 Code-Lösung

import oracledb

verbindung = oracledb.connect(
    user="Lernen",
    password=input("Gib dein Kennwort ein: "),
    dsn="localhost:1521/FREEPDB1"
)
cursor = verbindung.cursor()

# Datei lesen und zeilenweise verarbeiten
with open("bestellungen.txt", "r", encoding="utf-8") as datei:
    for zeile in datei:
        spalten = zeile.strip().split(",")

        prod_description = spalten[1]
        prod_preis = float(spalten[2])
        prod_kategorie = "Elektronik"

        # SQL Statement mit Bind-Variablen (OHNE Semikolon am Ende!)
        tsql = "INSERT INTO PRODUKTE (NAME, PREIS_NETTO, KATEGORIE) VALUES (:1, :2, :3)"

        # Parameter als Tupel in cursor.execute übergeben
        cursor.execute(tsql, (prod_description, prod_preis, prod_kategorie))

# Änderungen in der Datenbank speichern
verbindung.commit()
print("✅ Alle Produkte sind erfolgreich in die Datenbank geschrieben worden.")

# Schließen
cursor.close()
verbindung.close()
💡 Erkenntnisse

✅ Kein Semikolon in cursor.execute(): SQL-Strings in Python DB-APIs dürfen am Ende kein Semikolon ; enthalten (sonst ORA-00911).
✅ Parameter als Tupel: Die Werte für Bind-Variablen müssen als Tupel (val1, val2, val3) an cursor.execute(sql, ...) übergeben werden.
✅ Sichere Kennwortabfrage: Das Passwort kann mit input() interaktiv abgefragt werden.

Lektion 21 – Fehler-Logging & Robuster CSV-Import

📚 Gelernt

Absichern von einzelnen Schleifendurchläufen durch einen inneren try / except ValueError:-Block
Fortsetzen der Schleife bei fehlerhaften Datensätzen mittels continue
Protokollieren von fehlerhaften Zeilen und Ausnahmegründen in einer Log-Datei (import_fehler.log) im Anhänge-Modus ("a")
Einbinden dynamischer Dateinamen (FILENAME) in Log-Einträge
Vermeidung von unbeabsichtigten Tupeln bei Variable-Zuweisungen (z. B. Kommas am Zeilenende bei PASSCODE)
💻 Übungen

Erstellung eines erweiterten Import-Skripts bestellungen_2.txt mit innerem try / except ValueError:, automatischer Logfile-Generierung (import_fehler.log) und robuster Fehlerbehandlung bei der Datentyp-Umwandlung.
💡 Erkenntnisse

✅ Ein inneres try / except verhindert, dass eine einzelne defekte Zeile den gesamten Importprozess abbricht.
✅ Im "a"-Modus (Append) werden neue Fehler an die Log-Datei angehängt, ohne alte Protokolle zu überschreiben.
✅ Alle Konvertierungen (float(), .upper()) gehören in den try-Block, damit Fehler zuverlässig abgefangen werden.

🎯 Status

✅ Verstanden

Lektion 22 – DB-Schema- & Datenanalyse sowie PDF-Strukturzuordnung

📚 Gelernt

Automatisierter Export von Oracle-Metadaten (USER_TAB_COLUMNS) und Beispieldaten (FETCH FIRST 5 ROWS ONLY) via Python-Skript
Analyse von Datums- und Zahlenformaten (ISO-Timestamp YYYY-MM-DD HH:MM:SS, Preise mit Punkt als Dezimaltrenner)
Zuordnung von externen PDF-Dokumenten zu Oracle-Zieltabellen:
Rechnungen (B949807855_RG.pdf) $\rightarrow$ RECHNUNGS_KOPF
Einzelverbindungsnachweise (..._egn.pdf) $\rightarrow$ RECHNUNGS_ZEILEN
Wissensüberprüfung: 83 % im Gesamttest (10/12 richtig)
💻 Übungen

Erstellung und Ausführung von export_schema.py (db_schema.txt) und export_sample_data.py (db_sample_data.txt).
Zuordnungsmatrix für PDF-Datenfelder zu Oracle-Spalten erstellt.
💡 Erkenntnisse

✅ Metadatenabfragen aus USER_TAB_COLUMNS ermöglichen das automatische Dokumentieren ganzer Datenbanken.
✅ RECHNUNGS_KOPF speichert Stammdaten, Summen und Dateinamen; RECHNUNGS_ZEILEN erfasst Einzelpositionen.
✅ input() liefert immer str zurück; Verkettung von String + Int führt zu TypeError.

🎯 Status

✅ Verstanden

Lektion 23 – PDF-Parsing mit pypdf, Anker-Prinzip & Text-Extraction

📚 Gelernt

PDF-Dateien mit pypdf.PdfReader öffnen und Seitenzahl ermitteln (len(reader.pages))
Text aus einzelnen PDF-Seiten extrahieren (reader.pages[0].extract_text())
Zerlegen des extrahierten Fließtexts in Zeilen-Listen mit .split("\n")
Analyse der internen PDF-Auslesereihenfolge durch nummerierte Ausgabe mit enumerate(seite_1_text)
Anker-Prinzip: Gezieltes Ansteuern von Werten über feste Schlüsselbegriffe in Kombination mit relativer Indexverschiebung (index + 1)
Exakte Zeilenabfrage mit == vs. Teilstring-Suche mit in (z. B. "Rechnung" == zeile schließt Rechtshinweise aus)
Säuberung von Extraktionswerten mit .strip() (verhindert das Löschen innerer Leerzeichen bei Tarifen/Namen gegenüber .replace())
Fließtext-Isolierung mit doppelter .split()-Abfolge zur Extraktion von Rechnungsbetrag (9,94) und Steuersatz (19)
💻 Code-Lösung

from pypdf import PdfReader

PFAD = "/Users/axelhoernschemeyer/Downloads/Oracle-Projekte/Mobilfunkvertragsauswertung/"
DATEI = "B949807855_RG.pdf"

reader = PdfReader(PFAD + DATEI)
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
        rechter_teil = zeile.split("in Höhe von ")[1]
        betrag = rechter_teil.split(" ")[0]

print(f"Kundennummer {kunden_nr} - Datum {rg_datum} - Rufnummer {rufnummer} - Tarif {tarif} - Rech.-Nr. {rg_nr} - Betrag {betrag} - Steuer {steuer}")
💡 Erkenntnisse

✅ pypdf liest visuelle Blöcke manchmal in geänderter Reihenfolge aus (z. B. steht der Rechnungs-Kopfblock mit Rechnungsnummer im extrahierten Text ganz unten).
✅ enumerate() ist das perfekte Werkzeug, um bei Suchtreffern über den Index index + 1 auf Folgewerte zuzugreifen.
✅ .strip() entfernt nur Ränder-Leerzeichen, .replace(" ", "") löscht unkontrolliert auch Binnen-Leerzeichen.
✅ Fließtext-Ketten wie "in Höhe von 9,94 EUR" lassen sich sauber zerlegen: .split("in Höhe von ")[1].split(" ")[0].

🎯 Status

✅ Verstanden

Lektion 24 – Modulare Architektur & Rechnungs-Parsing (pdf_utils, get_vendor, get_invoice_details, main)

📚 Gelernt

Modulare Software-Architektur: Aufteilen eines komplexen Projekts in unabhängige Spezial-Module (pdf_utils.py, get_vendor.py, get_invoice_details.py, datenbank.py) und Orchestrierung in der Steuerzentrale (main.py).
Aufgabenteilung von Parametern & return:
Parameter in (...) sind ausschließlich Liefereingänge (Eingabe-Daten). Parameter-Namen sind frei wählbare Platzhalter innerhalb der Funktion.
Das Schlüsselwort return ist ausschließlich die Warenausgabe (Ergebnis-Rückgabe nach außen).
Zentrales PDF-Einlesen (pdf_utils.py): Kapselung von pypdf.PdfReader in der Funktion lese_pdf_datei(datei_pfad), um das Dokument nur 1x im Speicher auszulesen und als Zeilen-Liste (split("\n")) an andere Funktionen weiterzureichen.
Robustes Kreditor-Matching (get_vendor.py): Verschachtelte Schleife (for kreditor in kreditoren_liste: / for zeile in text_inhalt_pdf:), die per if kreditor in zeile: Firmennamen selbst dann erkennt, wenn Zusatzwörter (z. B. "Absender:") in derselben Zeile stehen.
Anbieterspezifisches Parsing (get_invoice_details.py):
Einsatz von Python 3.10+ match / case aussteller: zur Erweiterung um zukünftige Rechnungssteller (Telekom, Vodafone, Drillisch).
Nutzen von Python Dictionaries (details = {}), um extrahierte Rechnungsdetails (Kunden-Nr., Rechnungsdatum, Rufnummer, Tarif, Rechnungsnummer, USt-Satz, Rechnungsbetrag) strukturieren und ohne Duplikate zurückzugeben.
Robuste String-Prüfungen (z. B. teil.startswith("B"), len(teil) >= 8, teil[1:].isdigit()), um falsche Fließtext-Treffer wie "Beanstandungen" als Rechnungsnummer auszuschließen.
Hauptprogramm (main.py): Sauberer Import der eigenen Module (import module as alias) und fehlerfreier Gesamttest.
💻 Code-Lösungen

1. pdf_utils.py (Zentraler PDF-Leser)

""" Hilfsfunktionen für die PDF-Verarbeitung """
from pypdf import PdfReader

def lese_pdf_datei(datei_pfad):
    """ Liest die erste Seite einer PDF aus und gibt die Zeilen als Liste zurück. """
    reader = PdfReader(datei_pfad)
    inhalt_pdf = reader.pages[0].extract_text().split("\n")
    return inhalt_pdf
2. get_vendor.py (Kreditoren-Erkennung)

""" Aussteller-Erkennung für Rechnungsdokumente """

def erkenne_aussteller(text_inhalt_pdf, kreditoren_liste):
    """ Ermittelt den Kreditor anhand des Textes auf der ersten Seite. """
    for kreditor in kreditoren_liste:
        for zeile in text_inhalt_pdf:
            if kreditor in zeile:
                return kreditor

    return "Kreditor nicht gefunden"
3. get_invoice_details.py (Rechnungsdetails-Extraktion)

""" Funktionen zur Extraktion von Rechnungsdetails aus PDF-Dateien """

def erkenne_rechnungsdetails(text_inhalt_pdf, aussteller):
    """ Ermittelt die Rechnungsdetails anhand des Textes auf der ersten Seite. """
    details = {}
    match aussteller:
        case "Drillisch Online GmbH":
            for index, zeile in enumerate(text_inhalt_pdf):
                if "Kunden Nr." in zeile:
                    details["Kunden-Nr."] = text_inhalt_pdf[index + 1].strip()
                elif "Datum" in zeile:
                    details["Rechnungsdatum"] = text_inhalt_pdf[index + 1].strip()
                elif "Rufnummer" in zeile:
                    details["Rufnummer"] = text_inhalt_pdf[index + 1].strip()
                elif "Tarif" in zeile:
                    details["Tarif"] = text_inhalt_pdf[index + 1].strip()
                elif "Rechnung" == zeile:
                    details["Rechnungsnummer"] = text_inhalt_pdf[index + 1].strip()
                elif "USt-Satz" in zeile:
                    details["USt-Satz"] = text_inhalt_pdf[index + 1].split(" ")[0]
                elif "in Höhe von" in zeile:
                    rechter_teil = zeile.split("in Höhe von ")[1]
                    betrag = rechter_teil.split(" ")[0]
                    details["Rechnungsbetrag"] = betrag
    return details
4. main.py (Steuerzentrale & Testlauf)

""" Hauptprogramm für die Rechnungseingang-Verarbeitung """

import datenbank as db
import pdf_utils as pdf
import get_vendor
import get_invoice_details as inv_details

PFAD = "/Users/axelhoernschemeyer/Downloads/Oracle-Projekte/Mobilfunkvertragsauswertung/"
DATEI = "B949807855_RG.pdf"

# 1. Aussteller erkennen
aussteller = get_vendor.erkenne_aussteller(pdf.lese_pdf_datei(PFAD + DATEI), db.get_all_vendor())
print(f"Erkannter Aussteller: {aussteller}")

# 2. Rechnungsdetails extrahieren
details = inv_details.erkenne_rechnungsdetails(pdf.lese_pdf_datei(PFAD + DATEI), aussteller)
print(f"Erkannte Rechnungsdetails: {details}")
💡 Erkenntnisse

✅ Parameter regeln nur die Eingabe, return regelt nur die Ausgabe.
✅ Ein zentraler PDF-Leser spart Rechenzeit und verhindert mehrfaches Öffnen derselben Datei.
✅ Dictionaries (details = {}) sind der perfekte Datentyp für strukturierte Schlüsselergebnisse.
✅ match / case hält den Code bei verschiedenen Rechnungsstellern extrem sauber und übersichtlich.

🎯 Status

✅ Verstanden

Lektion 25 – Oracle-Import (RECHNUNGS_KOPF), DB-IDs, Dynamic Exceptions & shutil-Archivierung

📚 Gelernt

Stammdaten-IDs aus Oracle auflösen (datenbank.py):
Erstellung der Funktion get_vendor_id(vendor_name, pwd) für SELECT ID FROM KREDITOREN WHERE NAME = :1.
Erstellung der Funktion get_tarif_id(tarif_name, pwd) für SELECT ID FROM TARIFE WHERE BEZEICHNUNG = :1.
Absicherung leerer Abfrageergebnisse über den Ternary Operator daten[0] if daten else None.
Datenbank-Import für Rechnungs-Kopfdaten (speichere_rechnung):
Ausführen von INSERT INTO RECHNUNGS_KOPF mit Bind-Variablen (:1, :2, :3...).
Datentyp-Konvertierung von Betrag & USt-Satz von String zu Float (float(val.replace(",", "."))).
SQL-Datumskonvertierung mit TO_DATE(:3, 'DD.MM.YYYY').
Robuste Fehlerbehandlung mit try / except oracledb.DatabaseError as e: und error, = e.args, um Datenbankmeldungen (z. B. Fremdschlüsselverletzungen bei fehlenden Tarifen) sauber im Terminal auszugeben (error.message).
Automatische Datei-Archivierung (shutil.move):
Verschieben erfolgreich verarbeiteter PDF-Dateien aus dem Eingangsordner in das Archivverzeichnis: shutil.move(PATH + FILE, ARCHIVE + FILE).
Python Bytecode-Cache (__pycache__):
Erklärung der Funktionsweise des automatischen Bytecode-Caches (.pyc) für beschleunigte Modul-Imports und Aufnahme in .gitignore.
💻 Code-Lösungen

1. get_vendor_id & get_tarif_id in datenbank.py

def get_vendor_id(vendor_name, pwd):
    """ ID des Kreditoren auslesen und zurückgeben. """
    verbindung = oracledb.connect(user=config.DB_USER, password=pwd, dsn=config.DSN)
    cursor = verbindung.cursor()
    cursor.execute("SELECT ID FROM KREDITOREN WHERE NAME = :1", (vendor_name,))
    daten = cursor.fetchone()
    cursor.close()
    verbindung.close()
    return daten[0] if daten else None

def get_tarif_id(tarif_name, pwd):
    """ ID des Tarifs auslesen und zurückgeben. """
    verbindung = oracledb.connect(user=config.DB_USER, password=pwd, dsn=config.DSN)
    cursor = verbindung.cursor()
    cursor.execute("SELECT ID FROM TARIFE WHERE BEZEICHNUNG = :1", (tarif_name,))
    daten = cursor.fetchone()
    cursor.close()
    verbindung.close()
    return daten[0] if daten else None
2. speichere_rechnung in datenbank.py

def speichere_rechnung(kreditor_id, tarif_id, details, pwd):
    """ Rechnung in der Oracle-Datenbank speichern. """
    try:
        verbindung = oracledb.connect(user=config.DB_USER, password=pwd, dsn=config.DSN)
        cursor = verbindung.cursor()

        betrag_netto = float(details.get("Rechnungsbetrag", "0").replace(",", "."))
        ust_satz = float(details.get("USt-Satz", "0").replace(",", "."))

        sql = """
            INSERT INTO RECHNUNGS_KOPF (
                KREDITOR_ID, KUNDEN_NUMMER, RG_DATUM, RUFNUMMER,
                TARIF_ID, RG_NUMMER, UST_SATZ, BETRAG_BRUTTO
            )
            VALUES (:1, :2, TO_DATE(:3, 'DD.MM.YYYY'), :4, :5, :6, :7, :8)
        """
        cursor.execute(sql, (
            kreditor_id,
            details.get("Kunden-Nr.", ""),
            details.get("Rechnungsdatum", ""),
            details.get("Rufnummer", ""),
            tarif_id,
            details.get("Rechnungsnummer", ""),
            ust_satz,
            betrag_netto
        ))  
        verbindung.commit()
        cursor.close()
        verbindung.close()
        print("✅ Rechnung erfolgreich in Oracle gespeichert!")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"❌ Datenbankfehler: {error.message}")
3. PDF-Archivierung in main.py

import shutil

# Verschieben der Datei in das Archivverzeichnis nach erfolgreichem Import
shutil.move(PATH + FILE, ARCHIVE + FILE)
print(f"📦 Datei {FILE} erfolgreich ins Archiv verschoben.")
💡 Erkenntnisse

✅ SELECT ID FROM ... WHERE NAME = :1 löst Freitext-Namen in relationale Fremdschlüssel auf.
✅ oracledb.DatabaseError mit error.message fängt ORA-Fehler (z. B. ORA-02291 Schlüsselverletzung) elegant und benutzerfreundlich ab.
✅ shutil.move(quelle, ziel) sorgt für saubere Dateiverwaltung nach dem Import.
✅ __pycache__ wird von Python automatisch erzeugt und gehört in .gitignore.

🎯 Status

✅ Verstanden

📊 Zusammenfassung & Aktueller Lernstand

Thema / Konzept	Status
Variablen & Ausgaben (print)	✅
Grunddatentypen & type()	✅
Rechenoperatoren (+, -, *, /, //, %)	✅
Benutzereingaben (input()) & Typumwandlung	✅
Verzweigungen (if, elif, else) & Logik (and, or)	✅
Schleifen (while & for)	✅
Listen & Listenfunktionen (len, sum, min, max)	✅
Verschachtelte Schleifen (Nested Loops)	✅
Praxisübung 01: Wochen-Wetterbericht	✅
Eigene Funktionen (def, return, Docstrings)	✅
Parameter & Standardwerte (Default Values)	✅
Mehrere Rückgabewerte & Unpacking (a, b, c = funktion())	✅
Dateizugriffe mit open(), with-Block, "w", "r", "utf-8"	✅
Zeilenweises Lesen, .strip(), .split(",") & Parsing	✅
Fehlerbehandlung (try / except, FileNotFoundError)	✅
Oracle-Anbindung (oracledb) & INSERT	✅
Praxisübung 02: Datei-Import in Oracle	✅
Lektion 21: Fehler-Logging & Robuster CSV-Import (import_fehler.log)	✅
Lektion 22: DB-Analyse & PDF-Zielzuordnung (RECHNUNGS_KOPF/ZEILEN)	✅
Lektion 23: PDF-Parsing mit pypdf, Anker-Prinzip & Fließtext-Isolierung	✅
Lektion 24: Modulare Architektur & Rechnungs-Parsing (pdf_utils, get_vendor, get_invoice_details, main)	✅
Lektion 25: Oracle-Import (RECHNUNGS_KOPF), DB-IDs, Dynamic Exceptions & shutil-Archivierung	✅
🎯 Nächste Meilensteine

🔜 Einzelverbindungsnachweise parsen (RECHNUNGS_ZEILEN): Auslesen der EGN-PDFs (..._egn.pdf) und Schreiben der Einzelpositionen in RECHNUNGS_ZEILEN
🔜 Ordnerüberwachung / Batch-Import: Mehrere PDF-Rechnungen automatisiert aus einem Ordner verarbeiten
Stand: Aktuelle Lerneinheit nach Lektion 25


