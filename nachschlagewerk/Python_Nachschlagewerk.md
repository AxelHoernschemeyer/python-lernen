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
- [9. Nützliche Befehle & Ausblick](#9-nützliche-befehle--ausblick)

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

```python
# and-Beispiel
if alter >= 18 and alter <= 66:
    print("Erwachsene Person im erwerbsfähigen Alter")

# or-Beispiel
if alter < 18 or alter >= 67:
    print("Sondergruppe (Kind/Jugendlicher oder Rentner)")
```

#### Wahrheitstabellen

```text
False and False -> False        False or False -> False
True  and False -> False        True  or False -> True
False and True  -> False        False or True  -> True
True  and True  -> True         True  or True  -> True
```

---

## 7. Schleifen (`while` & `for`)

### `while`-Schleife (Bedingungsgesteuert)

Wird ausgeführt, solange eine Bedingung `True` ist.

```python
# Vorwärts zählen
zahl = 1
while zahl <= 5:
    print(zahl)
    zahl += 1  # Kurzform für: zahl = zahl + 1

# Rückwärts zählen
zahl = 5
while zahl >= 1:
    print(zahl)
    zahl -= 1  # Kurzform für: zahl = zahl - 1
```

> ⚠️ **Achtung vor Endlosschleifen:**  
> Wird die Zählvariable nicht verändert, bleibt die Bedingung ewig `True`. Eine `while`-Schleife benötigt immer eine Veränderung, die die Bedingung irgendwann `False` werden lässt.

### `for`-Schleife (Anzahl-gesteuert mit `range()`)

Ideal, wenn die Anzahl der Wiederholungen im Voraus bekannt ist.

```python
# range(start, ende) -> Endwert ist EXKLUSIV (wird nicht erreicht)
for i in range(1, 6):
    print(i)  # Gibt 1, 2, 3, 4, 5 aus

# range(start, ende, schrittweite)
for i in range(0, 11, 2):
    print(i)  # Gibt 0, 2, 4, 6, 8, 10 aus

# Rückwärts zählen mit negativer Schrittweite
for i in range(10, 0, -1):
    print(i)  # Gibt 10 bis 1 aus
```

### Praxis-Vergleich: `while` vs. `for`

| Merkmal | `while`-Schleife | `for`-Schleife |
| :--- | :--- | :--- |
| **Einsatzbereich** | Wenn Wiederholungsanzahl unklar ist | Wenn Anzahl der Durchläufe bekannt ist |
| **Zähler** | Muss manuell erstellt & erhöht werden | Wird automatisch von `range()` / Liste gesteuert |

---

## 8. Listen

Eine Liste speichert mehrere Werte geordnet in einer einzigen Variable.

### Erstellen & Zugreifen

```python
staedte = ["Belm", "Osnabrück", "Bohmte"]

# Auf Elemente über den Index zugreifen (beginnt bei 0):
print(staedte[0])  # "Belm"
print(staedte[1])  # "Osnabrück"
```

> 💡 **Merksätze:**  
> - Indizes beginnen immer bei **0**.  
> - Negative Indizes zählen vom Ende: `staedte[-1]` liefert das **letzte** Element.

### Bearbeiten & Hinzufügen

```python
# Element ändern
staedte[2] = "Berlin"  # Ersetzt "Bohmte" durch "Berlin"

# Neues Element am Ende anfügen
staedte.append("Hamburg")

# Anzahl der Elemente ermitteln
anzahl = len(staedte)
print(f"Anzahl Städte: {anzahl}")
```

### Häufiger Fehler: `IndexError`

```python
print(staedte[10])  # ❌ IndexError: list index out of range
```

---

## 9. Nützliche Befehle & Ausblick

### Terminal-Befehle

```bash
# Python-Version prüfen:
python3 --version

# Python-Skript ausführen:
python3 dateiname.py
```

### Ausblick auf kommende Lektionen

- 🔜 **Lektion 11:** Schleifen mit Listen kombinieren (`for stadt in staedte:`)
- 🔜 **Funktionen** (`def meine_funktion():`)
- 🔜 **Dateizugriffe** (Dateien lesen & schreiben)
- 🔜 **Fehlerbehandlung** (`try / except`)
- 🔜 **Module & Datenbanken** (Oracle, PDF-Auswertungen)

---