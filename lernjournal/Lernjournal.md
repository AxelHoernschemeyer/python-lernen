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
- [ Zwischenprüfung 01](#-zwischenprüfung-01)
- [Lektion 08 – Schleifen mit `while`](#lektion-08--schleifen-mit-while)
- [Lektion 09 – `for`-Schleifen](#lektion-09--for-schleifen)
- [Lektion 10 – Listen](#lektion-10--listen)
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

## 📊 Zusammenfassung & Aktueller Lernstand

| Thema / Konzept | Status |
| :--- | :---: |
| Variablen & Ausgaben (`print`) | ✅ |
| Grunddatentypen (`str`, `int`, `float`, `bool`) & `type()` | ✅ |
| Rechenoperatoren, Ganzzahldivision (`//`), Modulo (`%`) | ✅ |
| Benutzereingaben (`input()`) & Typumwandlung (`int()`, `float()`, `round()`) | ✅ |
| Verzweigungen (`if`, `elif`, `else`) & Logik (`and`, `or`) | ✅ |
| `while`-Schleifen & Zähler | ✅ |
| `for`-Schleifen & `range()` (inkl. Schrittweiten) | ✅ |
| Listen (Indizes ab `0`, `.append()`, `len()`, negative Indizes) | ✅ |

---

## 🎯 Nächste Meilensteine

- 🔜 **Lektion 11:** Schleifen mit Listen kombinieren (Gefilterte Ausgaben)
- 🔜 Verschachtelte Schleifen
- 🔜 Erste kleine Praxisprojekte
- 🔜 Funktionen (`def`)
- 🔜 Dateizugriffe & Fehlerbehandlung (`try/except`)
- 🔜 PDF-Auswertung & Oracle-Anbindung

---

*Stand: Aktuelle Lerneinheit vor Lektion 11*
