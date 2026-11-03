# 🐍 Python Nachschlagewerk

> **Persönliches Nachschlagewerk für die Python-Ausbildung**  
> *Ziel:* Python verstehen, anwenden und eigene Programme entwickeln.

---

## 📌 Inhaltsverzeichnis

- [1. Variablen](#1-variablen)
- [2. Datentypen & Typprüfung](#2-datentypen--typprüfung)
- [3. Rechenoperatoren](#3-rechenoperatoren)
- [4. Datentyp-Umwandlung & String-Operationen](#4-datentyp-umwandlung--string-operationen)
- [5. Ein- und Ausgaben](#5-ein--und-ausgaben)
- [6. Bedingungen & Logische Operatoren](#6-bedingungen--logische-operatoren)
- [7. Schleifen (`while` & `for`)](#7-schleifen-while--for)
- [8. Listen](#8-listen)
- [9. Schleifen mit Listen](#9-schleifen-mit-listen)
- [10. Nützliche Listenfunktionen](#10-nützliche-listenfunktionen)
- [11. Verschachtelte Schleifen](#11-verschachtelte-schleifen)
- [12. Eigene Funktionen (`def`), Parameter & Mehrfach-Rückgabe](#12-eigene-funktionen-def-parameter--mehrfach-rückgabe)
- [13. Dateizugriffe (`open()`) & Text-Parsing](#13-dateizugriffe-open--text-parsing)
- [14. Fehlerbehandlung (`try / except`)](#14-fehlerbehandlung-try--except)
- [15. Oracle-Datenbankanbindung (`oracledb`)](#15-oracle-datenbankanbindung-oracledb)
- [16. Robuster Datei-Import mit Fehler-Logging](#16-robuster-datei-import-mit-fehler-logging)
- [17. Oracle-Metadaten & Beispieldaten auslesen](#17-oracle-metadaten--beispieldaten-auslesen)
- [18. PDF-Parsing mit `pypdf` & Text-Anker-Extraction](#18-pdf-parsing-mit-pypdf--text-anker-extraction)
- [19. Moderne Pfadverwaltung mit `pathlib` & Projektstruktur](#19-moderne-pfadverwaltung-mit-pathlib--projektstruktur)
- [20. Nützliche Befehle & Ausblick](#20-nützliche-befehle--ausblick)
- [21. Modulare Software-Architektur & `match/case`-Parsing](#21-modulare-software-architektur--matchcase-parsing)
- [22. Python-Interna & `__pycache__` (Bytecode-Cache)](#22-python-interna--pycache-bytecode-cache)
- [23. Oracle-Import (`RECHNUNGS_KOPF`), Stammdaten-IDs & `shutil`-Archivierung](#23-oracle-import-rechnungs_kopf-stammdaten-ids--shutil-archivierung)
- [22. Python-Interna & `__pycache__` (Bytecode-Cache)](#22-python-interna--__pycache__-bytecode-cache)

---

## 1. Variablen

Variables store values in memory. In Python, no explicit declaration is required—Python determines the data type automatically based on the assigned value.

```python
name = "Axel"
alter = 54

print(name, alter)
print("Mein Name:", name, "Mein Alter:", alter)
```

> 💡 **Merksatz:**  
> `Variable = Name für einen gespeicherten Wert im Arbeitsspeicher`

---

## 2. Datentypen & Typprüfung

### Die wichtigsten Grunddatentypen

| Datentyp | Kurzzeichen | Bedeutung | Beispiel |
| :--- | :--- | :--- | :--- |
| **String** | `str` | Text | `"Axel"` |
| **Integer** | `int` | Ganze Zahl | `54` |
| **Float** | `float` | Gleitkommazahl | `1.82` |
| **Boolean** | `bool` | Wahrheitswert | `True` / `False` |

### Beispiele & Datentyp mit `type()` prüfen

```python
name = "Axel"         # str
alter = 54            # int
groesse = 1.82        # float
verheiratet = True    # bool

# Datentypen abfragen:
print(type(name))         # <class 'str'>
print(type(alter))        # <class 'int'>
print(type(groesse))      # <class 'float'>
print(type(verheiratet))  # <class 'bool'>
```

---

## 3. Rechenoperatoren

### Grundrechenarten

```python
+   # Addition (z. B. 5 + 3 = 8)
-   # Subtraktion (z. B. 10 - 4 = 6)
*   # Multiplikation (z. B. 3 * 4 = 12)
/   # Division (z. B. 10 / 2 = 5.0 -> liefert immer float)
```

### Spezielle Operatoren

```python
//  # Ganzzahldivision (schneidet Nachkommastellen ab)
%   # Modulo (liefert den Rest einer Division)
**  # Potenzierung (berechnet Basis hoch Exponent)
```

**Beispiele:**
```python
print(20 // 3)  # Ergebnis: 6
print(20 % 3)   # Ergebnis: 2 (Rest von 20 / 3)
print(5 ** 2)   # Ergebnis: 25 (5 hoch 2)
```

> 💡 **Merksätze:**  
> - `%` (Modulo) liefert den **Rest** einer Division.  
> - `//` (Ganzzahldivision) entfernt alle Nachkommastellen ohne zu runden.  
> - `**` berechnet eine **Potenz**.

---

## 4. Datentyp-Umwandlung & String-Operationen

### Typumwandlung (`Typecasting`)

```python
# String zu Integer
zahl_text = "54"
zahl_int = int(zahl_text)

# String zu Float
komma_zahl = float("54.3")
```

### Unterschied: `int()` vs. `round()`

```python
int(54.9)    # Ergebnis: 54 (schneidet Nachkommastellen einfach ab)
round(54.9)  # Ergebnis: 55 (rundet kaufmännisch)
```

> 💡 **Merksatz:**  
> `int() = abschneiden` | `round() = runden`

### Fehlerquellen bei `int()`

```python
int("54")    # OK -> 54
int("Axel")  # Fehler! -> ValueError: invalid literal for int()
```

### String-Verknüpfung und Multiplikation

| Operation | Code | Ergebnis | Anmerkung |
| :--- | :--- | :--- | :--- |
| Text + Text | `"54" + "1"` | `"541"` | Konkatenation (Verbindung) |
| Zahl + Zahl | `54 + 1` | `55` | Mathematische Addition |
| Text * Zahl | `"Axel" * 3` | `"AxelAxelAxel"` | Textwiederholung |
| Text + Zahl | `"54" + 1` | ❌ `TypeError` | Nicht erlaubt! |

---

## 5. Ein- und Ausgaben

### Benutzereingaben mit `input()`

```python
name = input("Wie heißt du? ")
alter_str = input("Wie alt bist du? ")

# Umwandlung für Rechnungen notwendig:
alter_int = int(alter_str)
```

> 💡 **Merksatz:**  
> `input()` liefert **immer** einen String (`str`) zurück, selbst wenn eine Zahl eingegeben wird!

---

## 6. Bedingungen & Logische Operatoren

### Vergleichsoperatoren

| Operator | Bedeutung |
| :---: | :--- |
| `<` | kleiner als |
| `<=` | kleiner oder gleich |
| `>` | größer als |
| `>=` | größer oder gleich |
| `==` | gleich (Wertvergleich) |
| `!=` | ungleich |

### Verkettete Vergleiche (Chained Comparisons)

```python
if 20 <= temp <= 25:
    print("Angenehmes Wetter")
```

### Verzweigungen (`if`, `elif`, `else`)

```python
note = 2

if note == 1:
    print("Sehr gut")
elif note == 2:
    print("Gut")
elif note == 3:
    print("Befriedigend")
else:
    print("Unbekannte Note")
```

> 💡 **Wichtig:**  
> Bei `if / elif / else` arbeitet Python von oben nach unten und führt **nur den ersten zutreffenden Zweig** aus.

### Logische Operatoren (`and`, `or`)

- **`and`**: Beide Bedingungen müssen wahr (`True`) sein.
- **`or`**: Mindestens eine Bedingung muss wahr (`True`) sein.

---

## 7. Schleifen (`while` & `for`)

### `while`-Schleife (Bedingungsgesteuert)

```python
zahl = 1
while zahl <= 5:
    print(zahl)
    zahl += 1
```

### `for`-Schleife (Anzahl-gesteuert mit `range()`)

```python
for i in range(1, 6):
    print(i)  # Gibt 1 bis 5 aus
```

---

## 8. Listen

Eine Liste speichert mehrere Werte geordnet in einer einzigen Variable.

```python
staedte = ["Belm", "Osnabrück", "Bohmte"]
print(staedte[0])   # "Belm"
print(staedte[-1])  # "Bohmte" (letztes Element)
staedte.append("Hamburg")
```

---

## 9. Schleifen mit Listen

```python
for stadt in staedte:
    print(stadt)
```

---

## 10. Nützliche Listenfunktionen

| Funktion | Beschreibung | Beispiel | Ergebnis |
| :--- | :--- | :--- | :--- |
| `len(liste)` | Anzahl der Elemente | `len([1, 2, 3])` | `3` |
| `sum(liste)` | Summe aller Elemente | `sum([1, 2, 3])` | `6` |
| `min(liste)` | Kleinstes Element | `min([1, 2, 3])` | `1` |
| `max(liste)` | Größtes Element | `max([1, 2, 3])` | `3` |

---

## 11. Verschachtelte Schleifen

```python
vornamen = ["Axel", "Lena"]
nachnamen = ["Müller", "Weber"]

for name in vornamen:
    for name2 in nachnamen:
        print(name, name2)
```

---

## 12. Eigene Funktionen (`def`), Parameter & Mehrfach-Rückgabe

### Basic Funktion mit `def` und Docstring
```python
def quadrat(zahl):
    """Berechnet das Quadrat einer Zahl."""
    return zahl * zahl
```

### Parameter mit Standardwerten & Mehrfach-Rückgabe (Unpacking)
```python
def statistik(zahlen, mwst=19):
    summe = sum(zahlen)
    anzahl = len(zahlen)
    schnitt = round(summe / anzahl, 2)
    return summe, anzahl, schnitt

# Aufruf & Unpacking:
gesamtsumme, anzahl, schnitt = statistik([10, 20, 30])
```

---

## 13. Dateizugriffe (`open()`) & Text-Parsing

### Schreiben und Lesen mit `with open()`
```python
# Schreiben ("w"):
with open("datei.txt", "w", encoding="utf-8") as datei:
    datei.write("Zeile 1\nZeile 2")

# Lesen ("r"):
with open("datei.txt", "r", encoding="utf-8") as datei:
    inhalt = datei.read()
```

### Zeilenweises Lesen & CSV-Parsing
```python
with open("daten.csv", "r", encoding="utf-8") as datei:
    for zeile in datei:
        spalten = zeile.strip().split(",")
        print(f"ID: {spalten[0]}, Name: {spalten[1]}, Wert: {spalten[2]}")
```

> 💡 **Merksätze:**  
> - `with open(...)` schließt die Datei automatisch.  
> - `encoding="utf-8"` sichert plattformübergreifend Umlaute und Sonderzeichen.  
> - `.strip()` entfernt Zeilenumbrüche (`\n`) und Leerzeichen an den Rändern.  
> - `.split(",")` zerlegt eine Zeichenkette am Trennzeichen in eine Liste.

---

## 14. Fehlerbehandlung (`try / except`)

```python
try:
    with open("daten.csv", "r", encoding="utf-8") as datei:
        inhalt = datei.read()
except FileNotFoundError:
    print("Fehler: Datei existiert nicht!")
except Exception as e:
    print(f"Unerwarteter Fehler: {e}")
```

---

## 15. Oracle-Datenbankanbindung (`oracledb`)

### Verbindungsaufbau & Abfrage
```python
import oracledb

verbindung = oracledb.connect(
    user="Lernen",
    password="dein_passwort",
    dsn="localhost:1521/FREEPDB1"
)
cursor = verbindung.cursor()

# SELECT
cursor.execute("SELECT SYSDATE FROM DUAL")
ergebnis = cursor.fetchone()
print(ergebnis[0])

cursor.close()
verbindung.close()
```

---

## 16. Robuster Datei-Import mit Fehler-Logging

### CSV-Parsing + Oracle `INSERT` + Logfile
```python
import oracledb

FILENAME = "bestellungen.txt"

try:
    with open(FILENAME, "r", encoding="utf-8") as datei:
        verbindung = oracledb.connect(
            user="Lernen",
            password=input("Passwort: "),
            dsn="localhost:1521/FREEPDB1"
        )
        cursor = verbindung.cursor()

        for zeile in datei:
            spalten = zeile.strip().split(",")

            try:
                prod_desc = spalten[1]
                prod_preis = float(spalten[2])
                prod_kat = spalten[3].upper()

                tsql = "INSERT INTO PRODUKTE (NAME, PREIS_NETTO, KATEGORIE) VALUES (:1, :2, :3)"
                cursor.execute(tsql, (prod_desc, prod_preis, prod_kat))

            except (ValueError, IndexError) as e:
                with open("import_fehler.log", "a", encoding="utf-8") as logfile:
                    logfile.write(f"[{FILENAME}] Fehlerhafte Zeile: {zeile.strip()} | Grund: {e}\n")
                continue

        verbindung.commit()
        cursor.close()
        verbindung.close()

except FileNotFoundError:
    print(f"Datei '{FILENAME}' nicht gefunden!")
except oracledb.Error as e:
    print(f"DB-Fehler: {e}")
```

> 💡 **Merksätze:**  
> - Innerer `try / except`-Block schützt vor Absturz einzelner Datenzeilen.  
> - Append-Modus `"a"` beim Logfile verhindert das Überschreiben alter Fehlermeldungen.  
> - Bind-Variablen `:1, :2` immer als Tupel `(val1, val2)` an `cursor.execute()` übergeben.

---

## 17. Oracle-Metadaten & Beispieldaten auslesen

### Schema-Export (`USER_TAB_COLUMNS`)
```python
cursor.execute("SELECT table_name, column_name, data_type FROM user_tab_columns ORDER BY table_name, column_id")
```

### Beispieldaten-Export (Oracle 12c+ Syntax)
```python
cursor.execute("SELECT * FROM tabelle FETCH FIRST 5 ROWS ONLY")
```

---

## 18. PDF-Parsing mit `pypdf` & Text-Anker-Extraction

### Öffnen & Text extrahieren
```python
from pypdf import PdfReader

reader = PdfReader("rechnung.pdf")
anzahl_seiten = len(reader.pages)

# Text der ersten Seite auslesen und zeilenweise zerlegen
seite_1_zeilen = reader.pages[0].extract_text().split("\n")
```

### Ankerwort-Parsing mit `enumerate()` und relativer Position (`index + 1`)
```python
for index, zeile in enumerate(seite_1_zeilen):
    if "Kunden Nr." in zeile:
        # Der Wert steht exakt in der Zeile darunter
        kunden_nr = seite_1_zeilen[index + 1].strip()
    elif "Rechnung" == zeile:
        # Exakte Prüfung mit == verhindert falsche Treffer in Sätzen
        rg_nr = seite_1_zeilen[index + 1].strip()
```

### Fließtext-Isolierung mit Verkettung von `.split()`
```python
elif "in Höhe von" in zeile:
    # "Wir buchen den Rechnungsbetrag in Höhe von 9,94 EUR..."
    betrag = zeile.split("in Höhe von ")[1].split(" ")[0]
```

> 💡 **Merksätze:**  
> - `pypdf` kann visuelle PDF-Textblöcke in geänderter Reihenfolge liefern $\rightarrow$ immer erst mit `enumerate()` analysieren!  
> - `.strip()` entfernt Leerzeichen am Anfang und Ende, lässt Binnen-Leerzeichen aber intakt.  
> - `zeile.split("anker")[1]` liefert alles rechts vom Ankerwort.

---

## 19. Moderne Pfadverwaltung mit `pathlib` & Projektstruktur

Das Python-Standardmodul `pathlib` bietet eine elegante, objektorientierte und plattformunabhängige Möglichkeit, Dateipfade zu verwalten.

```python
from pathlib import Path

# Bestimmt automatisch den Ordner, in dem die aktuelle Datei liegt:
BASE_DIR = Path(__file__).parent

# Unterordner dynamisch mit dem Division-Operator / verbinden:
INBOX_DIRECTORY = BASE_DIR / "inbox"
ARCHIV_DIRECTORY = BASE_DIR / "archiv"

# Prüfen, ob ein Pfad existiert oder eine Datei ist:
if INBOX_DIRECTORY.exists():
    print(f"Ordner vorhanden: {INBOX_DIRECTORY}")
```

> 💡 **Merksätze:**  
> - `Path(__file__).parent` ermittelt dynamisch das Verzeichnis der aktuellen Skriptdatei.  
> - Mit dem `/`-Operator können `Path`-Objekte direkt und plattformunabhängig (Windows `\`, macOS `/`) mit Ordner- und Dateinamen verknüpft werden.  
> - Projektweite Pfade gehören zentral in eine `config.py` in Großbuchstaben (`BASE_DIR`, `INBOX_DIRECTORY`).

---

## 20. Nützliche Befehle & Ausblick

### Terminal-Befehle
```bash
python3 -m pip install oracledb pypdf
python3 dateiname.py
```

### Nächste Schritte
- 🔜 **Aussteller-Erkennung (Fingerabdruck-System)**
- 🔜 **Modularisierung (Auslagerung von Parser-Funktionen)**
- 🔜 **Typumwandlung & SQL INSERT für `RECHNUNGS_KOPF`**

---

## 21. Modulare Software-Architektur & `match/case`-Parsing

### Parameter (Eingabe) vs. `return` (Ausgabe)
- **Parameter `(...)`**: Dienen **ausschließlich** dem Liefereingang (Daten in die Funktion hineinreichen). Parameter-Namen sind frei wählbare Platzhalter innerhalb der Funktion.
- **`return`**: Dient **ausschließlich** der Warenausgabe (Ergebnis nach außen zurückgeben).

```python
# Liefereingang: pdf_text, db_liste | Warenausgabe: Kreditor-String
def erkenne_aussteller(pdf_text, db_liste):
    for kreditor in db_liste:
        for zeile in pdf_text:
            if kreditor in zeile:
                return kreditor
    return "Kreditor nicht gefunden"
```

### Modul-Struktur & Orchestrierung in `main.py`

| Modul | Aufgabe | Hauptfunktion |
| :--- | :--- | :--- |
| `pdf_utils.py` | Einmaliges Einlesen von PDF-Seiten | `lese_pdf_datei(datei_pfad)` |
| `datenbank.py` | Oracle-DB-Verbindung & Stammdaten | `get_all_vendor()`, `get_vendor_id()`, `speichere_rechnung()` |
| `get_vendor.py` | Kreditor-Erkennung gegen DB-Liste | `erkenne_aussteller(pdf_text, db_liste)` |
| `get_invoice_details.py` | Extraktion von Kopfdaten per `match/case` | `erkenne_rechnungsdetails(pdf_text, aussteller)` |
| `main.py` | Steuerzentrale & Verknüpfung aller Module | Orchestrierung aller Aufrufe |

---

## 22. Python-Interna & `__pycache__` (Bytecode-Cache)

Sobald ein Python-Skript andere eigene Module über `import` lädt (z. B. `import datenbank`, `import pdf_utils`), erstellt Python im selben Ordner automatisch das Verzeichnis **`__pycache__`**.

### Wie funktioniert der Bytecode-Cache?
1. **Übersetzung in Bytecode:** Beim ersten Aufruf wandelt Python den lesbaren Quellcode der importierten Module (`.py`) in compilierten **Bytecode** (`.pyc`) um.
2. **Speicherung in `__pycache__`:** Dieser Bytecode wird als komprimierte Datei im Ordner `__pycache__/` abgelegt (z. B. `pdf_utils.cpython-312.pyc`).
3. **Schnellerer Programmstart:** Bei jedem weiteren Start von `main.py` prüft Python, ob sich die `.py`-Datei geändert hat. Wenn nicht, lädt Python direkt den `.pyc`-Bytecode aus dem Cache. Das spart die Analysezeit und beschleunigt den Start erheblich.

### Best Practice für Git & Repositories
- Der Ordner `__pycache__` enthält temporäre Laufzeitdateien und gehört **nicht** in die Git-Versionsverwaltung.
- **`.gitignore` Eintrag:**  
  ```text
  __pycache__/
  *.pyc
  ```

> 💡 **Merksatz:**  
> `__pycache__ = Automatischer Bytecode-Zwischenspeicher von Python für beschleunigte Modul-Imports.`

---

## 22. Python-Interna & `__pycache__` (Bytecode-Cache)

Beim Ausführen von Python-Skripten, die andere Module via `import` einbinden (z. B. `import datenbank`), erstellt Python automatisch den Ordner `__pycache__/`.

- **Funktionsweise:** Python übersetzt den Quellcode der importierten Skripte beim ersten Aufruf in compilierten **Bytecode** (`.pyc`-Dateien) und legt diesen im `__pycache__`-Ordner ab.
- **Vorteil:** Bei allen weiteren Programmstarts liest Python direkt den vorgefertigten Bytecode ein, anstatt die Dateien erneut zu parsen. Das beschleunigt den Start des Programms spürbar.
- **Versionsverwaltung (Git):** Da `__pycache__` maschinenspezifische Caches enthält, wird dieser Ordner nicht in Git hochgeladen, sondern in der `.gitignore`-Datei ausgeschlossen:

```text
# .gitignore
__pycache__/
*.pyc
```

---

## 23. Oracle-Import (`RECHNUNGS_KOPF`), Stammdaten-IDs & `shutil`-Archivierung

### Freitext in Stammdaten-IDs auflösen (`SELECT ID FROM ... WHERE NAME = :1`)
Relationale Datenbanken speichern Schlüssel-IDs (`KREDITOR_ID`, `TARIF_ID`) anstelle von Freitext-Bezeichnungen.

```python
def get_vendor_id(vendor_name, pwd):
    verbindung = oracledb.connect(user=config.DB_USER, password=pwd, dsn=config.DSN)
    cursor = verbindung.cursor()
    cursor.execute("SELECT ID FROM KREDITOREN WHERE NAME = :1", (vendor_name,))
    daten = cursor.fetchone()
    cursor.close()
    verbindung.close()
    return daten[0] if daten else None
```

> 💡 **Merksätze:**  
> - `daten[0] if daten else None` schützt vor einem `IndexError`, falls keine Treffer in der DB existieren.  
> - Bind-Variablen (`:1`, `:2`) schützen vor SQL-Injection.

### Rechnungs-Kopfdaten speichern & `oracledb.DatabaseError` abfangen
Werte aus Dictionaries (`details.get()`) mit `.replace(",", ".")` in `float` umwandeln und im SQL `TO_DATE()` nutzen:

```python
def speichere_rechnung(kreditor_id, tarif_id, details, pwd):
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
            kreditor_id, details.get("Kunden-Nr.", ""), details.get("Rechnungsdatum", ""),
            details.get("Rufnummer", ""), tarif_id, details.get("Rechnungsnummer", ""),
            ust_satz, betrag_netto
        ))
        verbindung.commit()
        cursor.close()
        verbindung.close()
        print("✅ Rechnung erfolgreich in Oracle gespeichert!")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"❌ Datenbankfehler: {error.message}")
```

### PDF-Datei ins Archiv verschieben (`shutil.move`)
Importierte Dateien zur Vermeidung von Mehrfach-Verarbeitungen ins Archiv verschieben:

```python
import shutil

shutil.move(PATH + FILE, ARCHIVE + FILE)
```

> 💡 **Merksatz:**  
> `shutil.move(quelle, ziel)` verschiebt Dateien sauber im Dateisystem.

```
