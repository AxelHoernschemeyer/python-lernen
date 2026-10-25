# 🐍 Python Lernjournal

> **Repository:** `python-lernen`  
> **Ziel:** Python von Grund auf lernen und sicher für Automatisierungen, Datenverarbeitung & Datenbankanbindungen anwenden.

---

## 📌 Inhaltsverzeichnis

- [Überblick & Ziele](#überblick--ziele)
- [Lektion 01 – Variablen und Ausgaben](#lektion-01--variablen-und-ausgaben)
- [Lektion 02 – Datentypen](#lektion-02--datentypen)
- [Lektion 03 – Rechnen mit Zahlen](#lektion-03--rechnen-mit-zahlen)
- [Lektion 04 – Benutzereingaben](#lektion-04--benutzereingaben)
- [Lektion 05 – Datentypen umwandeln](#lektion-05--datentypen-umwandeln)
- [Lektion 06 – Bedingungen mit `if`](#lektion-06--bedingungen-mit-if)
- [Lektion 07 – Bedingungen mit `elif` & logische Operatoren](#lektion-07--bedingungen-mit-elif--logische-operatoren)
- [📝 Zwischenprüfung 01](#-zwischenprüfung-01)
- [Lektion 08 – Schleifen mit `while`](#lektion-08--schleifen-mit-while)
- [Lektion 09 – `for`-Schleifen](#lektion-09--for-schleifen)
- [Lektion 10 – Listen](#lektion-10--listen)
- [Lektion 11 – Schleifen mit Listen](#lektion-11--schleifen-mit-listen)
- [Lektion 12 – Listenfunktionen & Berechnungen](#lektion-12--listenfunktionen--berechnungen)
- [Lektion 13 – Verschachtelte Schleifen](#lektion-13--verschachtelte-schleifen)
- [🛠️ Praxisübung 01 – Wochen-Wetterbericht](#️-praxisübung-01--wochen-wetterbericht)
- [Lektion 14 – Eigene Funktionen (`def`)](#lektion-14--eigene-funktionen-def)
- [Lektion 15 – Parameter & Standardwerte](#lektion-15--parameter--standardwerte)
- [Lektion 16 – Mehrere Rückgabewerte & Variable Unpacking](#lektion-16--mehrere-rückgabewerte--variable-unpacking)
- [Lektion 17 – Dateizugriffe (`open()`)](#lektion-17--dateizugriffe-open)
- [Lektion 18 – Zeilenweises Lesen & Text-Parsing](#lektion-18--zeilenweises-lesen--text-parsing)
- [Lektion 19 – Fehlerbehandlung (`try / except`)](#lektion-19--fehlerbehandlung-try--except)
- [Lektion 20 – Oracle-Datenbankanbindung (`oracledb`)](#lektion-20--oracle-datenbankanbindung-oracledb)
- [🛠️ Praxisübung 02 – Datei-Import in Oracle-Datenbank](#️-praxisübung-02--datei-import-in-oracle-datenbank)
- [Lektion 21 – Fehler-Logging & Robuster CSV-Import](#lektion-21--fehler-logging--robuster-csv-import)
- [📊 Zusammenfassung & Aktueller Lernstand](#-zusammenfassung--aktueller-lernstand)
- [🎯 Nächste Meilensteine](#-nächste-meilensteine)

---

## Überblick & Ziele

### 🚀 Langfristige Schwerpunkte
- Python-Grundlagen (Variablen, Bedingungen, Schleifen, Listen)
- Datentypen & Datenstrukturen
- Funktionen, Module & Dateiverarbeitung (`open()`, `read()`, `write()`)
- Fehlerbehandlung (`try` / `except`)
- Objektorientierte Programmierung (OOP)
- Automatisierung, PDF-Auswertungen & Datenbankanbindungen (Oracle)

### 🛠️ Praxisprojekte
- PDF-Rechnungen automatisiert auswerten
- Daten validieren & Fehler protokollieren
- Datenbanken anbinden & Importprozesse steuern

---

## Lektion 01 – Variablen und Ausgaben

### 📚 Gelernt
- Variablen anlegen und Werte zuweisen
- Texte und Zahlen mit `print()` ausgeben
- Variablen in Ausgaben kombinieren

### 💻 Übungen
- Persönliche Daten in Variablen gespeichert
- Eigene Textausgaben mit `print()` erstellt

### 💡 Erkenntnisse
✅ In Python müssen Variablen nicht explizit deklariert werden.  
✅ Python erkennt den Datentyp automatisch anhand des zugewiesenen Wertes.  
✅ Mehrere Werte können per Komma getrennt in `print()` ausgegeben werden.

### 🎯 Status
✅ Verstanden

---

## Lektion 02 – Datentypen

### 📚 Gelernt

| Datentyp | Beschreibung | Beispiel |
| :--- | :--- | :--- |
| `str` | Text (String) | `"Axel"` |
| `int` | Ganze Zahl (Integer) | `54` |
| `float` | Gleitkommazahl (Float) | `1.82` |
| `bool` | Wahrheitswert (Boolean) | `True` / `False` |

### 💻 Übungen
- Variablen mit verschiedenen Datentypen angelegt
- Datentypen mit `type()` überprüft

### 💡 Erkenntnisse
✅ Python unterscheidet strikt zwischen Text und Zahlen.  
✅ Identisch aussehende Inhalte können unterschiedliche Datentypen besitzen:
- `54` $\rightarrow$ `int`
- `"54"` $\rightarrow$ `str`
- `1.82` $\rightarrow$ `float`
- `True` $\rightarrow$ `bool`

### 🎯 Status
✅ Verstanden

---

## Lektion 03 – Rechnen mit Zahlen

### 📚 Gelernt
- Grundrechenarten: Addition (`+`), Subtraktion (`-`), Multiplikation (`*`), Division (`/`)
- Ganzzahldivision (`//`)
- Modulo (`%`)

### 💻 Übungen
- Rechnen mit Variablen
- Restwertbestimmung mit Modulo
- Ganzzahlige Ergebnisse ohne Nachkommastellen berechnen

### 💡 Erkenntnisse
✅ Modulo (`%`) liefert den Rest einer Division (z. B. `20 % 3` $\rightarrow$ `2`).  
✅ Ganzzahldivision (`//`) schneidet Nachkommastellen ab (z. B. `20 // 3` $\rightarrow$ `6`).  
✅ Strings können mit Integer multipliziert werden (z. B. `"Axel" * 3` $\rightarrow$ `"AxelAxelAxel"`).  
✅ Addition von String und Integer führt zu einem `TypeError` (z. B. `"5" + 1`).

### 🎯 Status
✅ Verstanden

---

## Lektion 04 – Benutzereingaben

### 📚 Gelernt
- Interaktive Benutzereingaben mit `input()`
- Verarbeitung und Ausgabe von Eingaben

### 💻 Übungen
- Vorname, Alter und Wohnort über die Konsole abgefragt
- Eingaben personalisiert ausgegeben

### 💡 Erkenntnisse
✅ `input()` liefert **immer** einen String (`str`) zurück – selbst wenn der Benutzer eine Zahl eingibt.  
✅ Zahlen aus `input()` müssen vor mathematischen Rechnungen umgewandelt werden.

### 🎯 Status
✅ Verstanden

---

## Lektion 05 – Datentypen umwandeln

### 📚 Gelernt
- Typumwandlung mit `int()` und `float()`
- Unterscheidung zwischen `int()` und `round()`

### 💻 Übungen
- Benutzereingaben in Zahlen umgewandelt und mathematisch berechnet
- Verhalten bei Nachkommastellen getestet

### 💡 Erkenntnisse
✅ `int()` wandelt Strings in Ganzzahlen um und schneidet Nachkommastellen ab (`int(54.9)` $\rightarrow$ `54`).  
✅ `round()` rundet kaufmännisch (`round(54.9)` $\rightarrow$ `55`).  
✅ Nur Strings, die reine Ziffern enthalten, können mit `int()` umgewandelt werden (andernfalls `ValueError`).

### 🎯 Status
✅ Verstanden

---

## Lektion 06 – Bedingungen mit `if`

### 📚 Gelernt
- Vergleichsoperatoren (`<`, `<=`, `>`, `>=`, `==`, `!=`)
- Verzweigungen mit `if` und `else`

### 💻 Übungen
- Prüfen von Volljährigkeit und Minderjährigkeit

### 💡 Erkenntnisse
✅ Bedingungen ergeben immer den Wahrheitswert `True` oder `False`.  
✅ `=` ist die Wertzuweisung, `==` ist der Wertvergleich.  
✅ Mit `else` wird der Alternativzweig ausgeführt, wenn die `if`-Bedingung nicht zutrifft.

### 🎯 Status
✅ Verstanden

---

## Lektion 07 – Bedingungen mit `elif` & logische Operatoren

### 📚 Gelernt
- Mehrfachverzweigungen mit `elif`
- Logische Operatoren `and` und `or`

### 💻 Übungen
- Auswertung von Schulnoten
- Zuordnung von Altersgruppen
- Kombination mehrerer Bedingungen in einer Abfrage

### 💡 Erkenntnisse
✅ Python arbeitet `if / elif / else` von oben nach unten ab und führt **nur den ersten zutreffenden Zweig** aus.  
✅ `and`: Beide Bedingungen müssen wahr sein.  
✅ `or`: Mindestens eine Bedingung muss wahr sein.

### 🎯 Status
✅ Verstanden

---

## 📝 Zwischenprüfung 01

### 📚 Geprüfte Themen
Variablen, Datentypen, Rechenoperatoren, Benutzereingaben, Typumwandlung, Verzweigungen (`if`/`elif`/`else`), Vergleichsoperatoren, `and`, `or`.

### 🏆 Ergebnis
**9 von 10 Punkten**

### 💡 Erkenntnisse
✅ Grundlegende Syntax und Logik sicher beherrscht.  
⚠️ Wichtiger Merksatz für die Zukunft: Aufgabenstellungen genau und vollständig lesen.

### 🎯 Status
✅ Bestanden

---

## Lektion 08 – Schleifen mit `while`

### 📚 Gelernt
- Bedingungsgesteuerte Schleifen mit `while`
- Zählvariablen und Kurzschreibweisen (`+= 1`, `-= 1`)
- Vermeidung von Endlosschleifen
- Kombination von Schleifen und `if`-Bedingungen

### 💻 Übungen
- Vorwärts- und Rückwärtszählen
- Berechnung von Quadratzahlen
- Unterscheidung gerader und ungerader Zahlen
- Dynamische Schleifendurchläufe mit Benutzereingabe

### 💡 Erkenntnisse
✅ `while`-Schleifen laufen, solange die Bedingung `True` bleibt.  
✅ Die Zählvariable muss innerhalb der Schleife angepasst werden, um Endlosschleifen zu vermeiden.

### 🎯 Status
✅ Verstanden

---

## Lektion 09 – `for`-Schleifen

### 📚 Gelernt
- Anzahlgesteuerte Schleifen mit `for`
- Zahlenbereiche erzeugen mit `range(start, ende, schrittweite)`
- Rückwärts zählen mit negativer Schrittweite

### 💻 Übungen
- Zahlenreihen ausgeben (1 bis 10)
- Gerade Zahlen mit Schrittweite `2` ausgeben
- Rückwärts zählen (10 bis 1)

### 💡 Erkenntnisse
✅ Ideal, wenn die Anzahl der Durchläufe im Voraus bekannt ist.  
✅ Bei `range(start, ende)` ist der Endwert **exklusiv** (wird nicht erreicht).

### 🎯 Status
✅ Verstanden

---

## Lektion 10 – Listen

### 📚 Gelernt
- Erstellen von Listen (`liste = [...]`)
- Lese- und Schreibzugriff über Indizes (beginnend bei `0`)
- Neue Elemente mit `.append()` hinzufügen
- Listenlänge bestimmen mit `len()`
- Zugriff vom Ende mit negativen Indizes (`-1`, `-2`)

### 💻 Übungen
- Städteliste angelegt und gepflegt
- Elemente geändert und erweitert
- Letztes Element per negativem Index ermittelt

### 💡 Erkenntnisse
✅ Indizes starten bei `0`.  
✅ `liste[-1]` greift direkt auf das letzte Element zu.  
✅ Nicht existierende Indizes lösen einen `IndexError: list index out of range` aus.

### 🎯 Status
✅ Verstanden

---

## Lektion 11 – Schleifen mit Listen

### 📚 Gelernt
- Iterieren über Listen mit `for element in liste:`
- Filtern von Listenwerten mit Bedingungen (`if`) innerhalb der Schleife
- Zugehörigkeitsprüfung mit `in` (z. B. `if note in [1, 2]:`)

### 💻 Übungen
- Filterung guter Noten (1 und 2) aus einer gegebenen Notenliste und formatierte Ausgabe.

### 💡 Erkenntnisse
✅ Schleifen greifen nacheinander auf jedes Element einer Liste zu.  
✅ Kombination aus `for` und `if` ermöglicht das gezielte Auswählen von Werten.

### 🎯 Status
✅ Verstanden

---

## Lektion 12 – Listenfunktionen & Berechnungen

### 📚 Gelernt
- Eingebaute Funktionen für numerische Listen: `len()`, `sum()`, `min()`, `max()`
- Berechnung von Statistiken (z. B. Notendurchschnitt: `summe / anzahl`)
- Kaufmännisches und ganzzahliges Runden von Ergebnissen mit `round()`

### 💻 Übungen
- Erfassung einer Notenliste, Ermittlung der Gesamtanzahl (`len`), Notensumme (`sum`) und Berechnung des gerundeten Notendurchschnitts.

### 💡 Erkenntnisse
✅ `sum(liste)` berechnet die Gesamtsumme aller Zahlen in einer Liste.  
✅ `len(liste)` gibt die Elementanzahl zurück.  
✅ Der Durchschnitt lässt sich direkt über `sum(liste) / len(liste)` ermitteln.

### 🎯 Status
✅ Verstanden

---

## Lektion 13 – Verschachtelte Schleifen

### 📚 Gelernt
- Konzept ineinander verschachtelter Schleifen (`Nested Loops`)
- Innere Schleife wird bei jedem Durchlauf der äußeren Schleife vollständig ausgeführt
- Kombination mehrerer Listen zur Erzeugung von Kreuzprodukten / Paarungen

### 💻 Übungen
- Kombination zweier Listen (`vornamen` und `nachnamen`) zur Ausgabe aller Namenskombinationen.

### 💡 Erkenntnisse
✅ Für jedes Element der äußeren Schleife wird die innere Schleife komplett durchlaufen.  
✅ Wenn die äußere Liste $N$ Elemente und die innere Liste $M$ Elemente hat, gibt es insgesamt $N \times M$ Durchläufe.

### 🎯 Status
✅ Verstanden

---

## 🛠️ Praxisübung 01 – Wochen-Wetterbericht

### 📚 Gelernt & Angewendet
- Praktische Kombination aus `for`-Schleifen, Akkumulatoren (`summe += temp`), verketteten Vergleichsoperatoren (`20 <= temp <= 25`) und `if/elif/else`
- Berechnung und Rundung von Durchschnittswerten über Listen (`round(summe / len(temperaturen), 1)`)

### 💻 Code-Lösung
```python
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
```

### 💡 Erkenntnisse
✅ Python erlaubt elegante verkettete Vergleiche wie `20 <= temp <= 25`.  
✅ Kombination aus Schleifen, Verzweigungen und mathematischen Funktionen festigt das Verständnis für reale Datenverarbeitungsprozesse.

### 🎯 Status
✅ Erfolgreich gelöst

---

## Lektion 14 – Eigene Funktionen (`def`)

### 📚 Gelernt
- Funktionen definieren mit `def funktion_name(parameter):`
- Codeblöcke wiederverwendbar kapseln (DRY-Prinzip: *Don't Repeat Yourself*)
- Ergebnisse mit `return` zurückgeben
- Dokumentation über Docstrings (`"""" ... """`)
- Beheben von Pylint-Warnungen (`missing-function-docstring`)

### 💻 Übungen
- Funktion `berechne_quadratzahl(zahl)` geschrieben, die das Quadrat berechnet und per `return` zurückgibt.
- Funktion mit Parameter `5` aufgerufen und Ergebnis ausgegeben (`25`).

### 💡 Erkenntnisse
✅ `def` leitet die Funktionsdefinition ein.  
✅ `return` beendet die Funktion und gibt den berechneten Wert an den Aufrufer zurück.  
✅ Klammern um den Rückgabewert bei `return` sind optional (Konvention in Python: `return ergebnis` ohne Klammern).

### 🎯 Status
✅ Verstanden

---

## Lektion 15 – Parameter & Standardwerte

### 📚 Gelernt
- Übergabe mehrerer Parameter an Funktionen
- Festlegen von Standardwerten (*Default Values*) bei der Funktionsdefinition (z. B. `mwst_satz=19`)
- Überschreiben von Standardwerten beim Aufruf durch explizite Argumente

### 💻 Übungen
- Erstellung der Funktion `berechne_preis(netto, mwst_satz=19)` zur Bruttoberechnung mit optional abweichendem Steuersatz.

### 💡 Erkenntnisse
✅ Wird ein Argument beim Aufruf weggelassen, greift automatisch der definierte Standardwert.  
✅ Werden alle Parameter beim Aufruf angegeben, wird der Standardwert für diesen Durchlauf überschrieben.

### 🎯 Status
✅ Verstanden

---

## Lektion 16 – Mehrere Rückgabewerte & Variable Unpacking

### 📚 Gelernt
- Rückgabe mehrerer kommagetrennter Werte aus einer Funktion (`return wert1, wert2, wert3`)
- Direktes Entpacken der Rückgabewerte in mehrere Variablen beim Aufruf (*Variable Unpacking*: `a, b, c = funktion()`)
- Vermeidung doppelter Berechnungen durch Zwischenvariablen innerhalb von Funktionen

### 💻 Übungen
- Funktion `berechne_statistik(zahlen_liste)` zur Ermittlung von Summe, Anzahl und gerundetem Durchschnitt aus einer Zahlenliste.

### 💡 Erkenntnisse
✅ Kommagetrennte `return`-Werte werden von Python als Tupel zurückgegeben und lassen sich beim Aufruf direkt entpacken.  
✅ Verwendung von lokalen Variablen (`gesamtsumme`, `anzahl`) erhöht Lesbarkeit und Performance.

### 🎯 Status
✅ Verstanden

---

## Lektion 17 – Dateizugriffe (`open()`)

### 📚 Gelernt
- Öffnen und Schließen von Dateien mit dem `with open(...) as datei:`-Block (automatisches Schließen/Ressourcenverwaltung)
- Modi: `"w"` (schreiben/überschreiben), `"a"` (anhängen), `"r"` (lesen)
- Zeichenkodierung mit `encoding="utf-8"` für plattformübergreifende Umlautsicherheit
- Schreiben mit `.write()` und Auslesen des gesamten Inhalts mit `.read()`

### 💻 Übungen
- Schreiben von zwei Logzeilen in `"log.txt"` im `"w"`-Modus und Auslesen des Inhalts im `"r"`-Modus.

### 💡 Erkenntnisse
✅ `with open()` stellt sicher, dass Dateien selbst bei Fehlern im Code sauber geschlossen werden.  
✅ `encoding="utf-8"` verhindert Umlaut-Fehler beim Wechsel zwischen Mac und Windows.

### 🎯 Status
✅ Verstanden

---

## Lektion 18 – Zeilenweises Lesen & Text-Parsing

### 📚 Gelernt
- Zeilenweises Iterieren über Dateien (`for zeile in datei:`) für speichereffiziente Verarbeitung großer Datenmengen
- Entfernen von unsichtbaren Steuerzeichen & Zeilenumbrüchen (`\n`) mit `.strip()`
- Zerschneiden von strukturierten Textzeilen (CSV-Prinzip) mit `.split(",")` in Listen
- Gezielter Zugriff auf Spalten über Indizes (`spalten[0]`, `spalten[1]`, etc.)
- Elegante Formatierung von Strings mit f-Strings (`f"Artikel: {spalten[1]} - Preis: {spalten[2]} €"`)

### 💻 Übungen
- Erstellung einer Bestellungsdatei `"bestellungen.txt"`, zeilenweises Einlesen, Zerlegen der Felder mit `.strip().split(",")` und formatierte Ausgabe im Terminal.

### 💡 Erkenntnisse
✅ Zeilenweises Lesen verbraucht kaum Arbeitsspeicher und eignet sich perfekt für große CSV-Dateien und spätere Datenbank-Imports.  
✅ Kombination aus `.strip()` und `.split(",")` zerlegt Rohdaten direkt in sauber verarbeitbare Spalten-Listen.

### 🎯 Status
✅ Verstanden

---

## Lektion 19 – Fehlerbehandlung (`try / except`)

### 📚 Gelernt
- Abfangen von Laufzeitfehlern (Exceptions) mit `try / except`
- Gezieltes Abfangen spezifischer Fehler wie `FileNotFoundError` oder `ValueError`
- Verhindern von unkontrollierten Programmabstürzen bei fehlenden Dateien oder ungültigen Eingaben

### 💻 Übungen
- Erstellung einer Fehlerabfrage mit `try:` und `except FileNotFoundError:`, um das Fehlen einer CSV-Export-Datei sauber abzufangen und eine verständliche Fehlermeldung auszugeben.

### 💡 Erkenntnisse
✅ `try:` umschließt den potenziell fehleranfälligen Codeabschnitt.  
✅ `except FileNotFoundError:` wird nur ausgeführt, wenn genau dieser Fehler auftritt.  
✅ Robuste Fehlerbehandlung ist essenziell für automatisierte Import-Skripte und Datenbankprozesse.

### 🎯 Status
✅ Verstanden

---

## Lektion 20 – Oracle-Datenbankanbindung (`oracledb`)

### 📚 Gelernt
- Installation von externen Python-Bibliotheken im Terminal über `python3 -m pip install oracledb`
- Importieren der Bibliotheken ganz oben im Skript (`import oracledb`)
- Verbindungsaufbau zur lokalen Oracle-Datenbank im Docker-Container (`oracledb.connect(user, password, dsn)`)
- Arbeiten mit dem Cursor (`verbindung.cursor()`) zum Ausführen von SQL-Abfragen (`cursor.execute()`)
- Ergebnisabfrage mit `cursor.fetchone()` und formatiertes Ausgeben mit f-Strings
- Sauberes Schließen von Cursor (`cursor.close()`) und Verbindung (`verbindung.close()`)

### 💻 Übungen
- Ausführen einer SQL-Abfrage (`SELECT SYSDATE FROM DUAL`) auf der lokalen Oracle-Datenbank und formatierte Ausgabe des Systemdatums.

### 💡 Erkenntnisse
✅ `import oracledb` muss zwingend vor der ersten Nutzung aufgerufen werden.  
✅ `cursor.fetchone()` liefert ein Ergebnis-Tupel zurück.  
✅ Das Schließen von Cursorn und Verbindungen gibt Ressourcen auf dem Datenbankserver wieder frei.

### 🎯 Status
✅ Verstanden

---

## 🛠️ Praxisübung 02 – Datei-Import in Oracle-Datenbank

### 📚 Gelernt & Angewendet
- Kombination aus Datei-Parsing (`open()`, `.strip().split(",")`) und Oracle-Datenbankimport (`oracledb`)
- Übergabe dynamischer Werte an SQL `INSERT` mit Bind-Variablen (`:1, :2, :3`) als Parameter-Tupel
- Transaktionssteuerung mit `verbindung.commit()` und sauberes Schließen von Cursor und Verbindung

### 💻 Code-Lösung
```python
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
```

### 💡 Erkenntnisse
✅ **Kein Semikolon in `cursor.execute()`:** SQL-Strings in Python DB-APIs dürfen am Ende kein Semikolon `;` enthalten (sonst `ORA-00911`).  
✅ **Parameter als Tupel:** Die Werte für Bind-Variablen müssen als Tupel `(val1, val2, val3)` an `cursor.execute(sql, ...)` übergeben werden.  
✅ **Sichere Kennwortabfrage:** Das Passwort kann mit `input()` interaktiv abgefragt werden.

---

## Lektion 21 – Fehler-Logging & Robuster CSV-Import

### 📚 Gelernt
- Absichern von einzelnen Schleifendurchläufen durch einen inneren `try / except ValueError:`-Block
- Fortsetzen der Schleife bei fehlerhaften Datensätzen mittels `continue`
- Protokollieren von fehlerhaften Zeilen und Ausnahmegründen in einer Log-Datei (`import_fehler.log`) im Anhänge-Modus (`"a"`)
- Einbinden dynamischer Dateinamen (`FILENAME`) in Log-Einträge
- Vermeidung von unbeabsichtigten Tupeln bei Variable-Zuweisungen (z. B. Kommas am Zeilenende bei `PASSCODE`)

### 💻 Übungen
- Erstellung eines erweiterten Import-Skripts `bestellungen_2.txt` mit innerem `try / except ValueError:`, automatischer Logfile-Generierung (`import_fehler.log`) und robuster Fehlerbehandlung bei der Datentyp-Umwandlung.

### 💡 Erkenntnisse
✅ Ein inneres `try / except` verhindert, dass eine einzelne defekte Zeile den gesamten Importprozess abbricht.  
✅ Im `"a"`-Modus (Append) werden neue Fehler an die Log-Datei angehängt, ohne alte Protokolle zu überschreiben.  
✅ Alle Konvertierungen (`float()`, `.upper()`) gehören **in** den `try`-Block, damit Fehler zuverlässig abgefangen werden.

### 🎯 Status
✅ Verstanden

---

## 📊 Zusammenfassung & Aktueller Lernstand

| Thema / Konzept | Status |
| :--- | :---: |
| Variablen & Ausgaben (`print`) | ✅ |
| Grunddatentypen & `type()` | ✅ |
| Rechenoperatoren (`+`, `-`, `*`, `/`, `//`, `%`) | ✅ |
| Benutzereingaben (`input()`) & Typumwandlung | ✅ |
| Verzweigungen (`if`, `elif`, `else`) & Logik (`and`, `or`) | ✅ |
| Schleifen (`while` & `for`) | ✅ |
| Listen & Listenfunktionen (`len`, `sum`, `min`, `max`) | ✅ |
| Verschachtelte Schleifen (`Nested Loops`) | ✅ |
| **Praxisübung 01: Wochen-Wetterbericht** | ✅ |
| Eigene Funktionen (`def`, `return`, Docstrings) | ✅ |
| Parameter & Standardwerte (*Default Values*) | ✅ |
| Mehrere Rückgabewerte & Unpacking (`a, b, c = funktion()`) | ✅ |
| Dateizugriffe mit `open()`, `with`-Block, `"w"`, `"r"`, `"utf-8"` | ✅ |
| Zeilenweises Lesen, `.strip()`, `.split(",")` & Parsing | ✅ |
| Fehlerbehandlung (`try / except`, `FileNotFoundError`) | ✅ |
| Oracle-Anbindung (`oracledb`) & `INSERT` | ✅ |
| **Praxisübung 02: Datei-Import in Oracle** | ✅ |
| **Lektion 21: Fehler-Logging & Robuster CSV-Import (`import_fehler.log`)** | ✅ |

---

## 🎯 Nächste Meilensteine

- 🔜 **Automatisierter Batch-Import & Ordnerüberwachung:** Mehrere Dateien aus einem Ordner verarbeiten
- 🔜 **PDF-Auswertung:** PDF-Rechnungen parsen und Daten automatisiert in Oracle ablegen

---

*Stand: Aktuelle Lerneinheit nach Lektion 21*

