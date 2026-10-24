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
- [14. Nützliche Befehle & Ausblick](#14-nützliche-befehle--ausblick)

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
    datei.write("Zeile 1
Zeile 2")

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
> - `.strip()` entfernt Zeilenumbrüche (`
`) und Leerzeichen an den Rändern.  
> - `.split(",")` zerlegt eine Zeichenkette am Trennzeichen in eine Liste.

---

## 14. Nützliche Befehle & Ausblick

### Terminal-Befehle
```bash
python3 dateiname.py
```

### Ausblick
- 🔜 **Fehlerbehandlung** (`try / except`)
- 🔜 **Oracle-Datenbankanbindung** (`oracledb`) & SQL-Imports
