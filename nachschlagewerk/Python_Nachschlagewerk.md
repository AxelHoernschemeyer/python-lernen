# 🐍 Python Nachschlagewerk

> Persönliches Nachschlagewerk für die Python-Ausbildung.
>
> Ziel: Python verstehen, anwenden und eigene Programme entwickeln.

---

# 📝 Variablen

Zuweisung und Ausgabe mit `print()`.

In Python ist keine separate Deklaration notwendig. Python bestimmt den Datentyp anhand des zugewiesenen Wertes automatisch.

```python
name = "Axel"
alter = 54

print(name, alter)
print("Mein Name:", name, "Mein Alter:", alter)
```

💡 Merksatz:

```text
Variable = Name für einen gespeicherten Wert
```

---

# 🔢 Datentypen

## Die wichtigsten Datentypen

| Datentyp | Bedeutung | Beispiel |
|-----------|-----------|-----------|
| `str` | Text | `"Axel"` |
| `int` | Ganze Zahl | `54` |
| `float` | Kommazahl | `1.82` |
| `bool` | Wahr/Falsch | `True` |

---

## 📝 String (str)

```python
name = "Axel"
alter = "54"
```

---

## 🔢 Integer (int)

```python
alter = 54
```

---

## 📏 Float (float)

```python
groesse = 1.82
```

---

## ✅ Boolean (bool)

```python
verheiratet = True
aktiv = False
```

---

## 🔍 Datentyp prüfen

```python
print(type(name))
print(type(alter))
print(type(groesse))
print(type(verheiratet))
```

---

# 🧮 Rechenoperatoren

```python
+   # Addition
-   # Subtraktion
*   # Multiplikation
/   # Division
```

## Weitere Operatoren

```python
//  # Ganzzahldivision
%   # Modulo (Rest)
**  # Potenz
```

### Beispiele

```python
20 // 3
# Ergebnis: 6
```

```python
20 % 3
# Ergebnis: 2
```

```python
5 ** 2
# Ergebnis: 25
```

💡 Merksätze:

```text
Modulo liefert den Rest einer Division.
```

```text
** berechnet eine Potenz.
```

---

# 🔄 Datentypen umwandeln

## String → Integer

```python
zahl = input("Zahl: ")

zahl = int(zahl)

print(zahl + 1)
```

## String → Float

```python
zahl = float("54.3")
```

---

## 📐 int() und round()

```python
int(54.9)
# Ergebnis: 54
```

```python
round(54.9)
# Ergebnis: 55
```

💡 Merksatz:

```text
int()   = abschneiden
round() = runden
```

---

## ⚠️ Fehler bei int()

Gültig:

```python
int("54")
```

Ungültig:

```python
int("Axel")
```

Fehler:

```text
ValueError
```

💡 Merksatz:

```text
Nur Texte, die wie Zahlen aussehen,
können mit int() umgewandelt werden.
```

---

# 🔤 Strings und Addition

## String + String

```python
"54" + "1"
```

Ergebnis:

```text
541
```

---

## String + Zahl

```python
"54" + 1
```

Ergebnis:

```text
TypeError
```

---

## String multiplizieren

```python
"Axel" * 5
```

Ergebnis:

```text
AxelAxelAxelAxelAxel
```

```python
"5" * 3
```

Ergebnis:

```text
555
```

💡 Merksatz:

```text
Text + Text = OK

Zahl + Zahl = OK

Text + Zahl = Fehler
```

---

# ⌨️ Ein- und Ausgaben

## Benutzereingaben

```python
name = input("Wie heißt du? ")
```

💡 Merksatz:

```text
input() liefert immer einen String (str) zurück.
```

Beispiel:

```python
alter = input("Alter: ")
```

Auch bei Eingabe:

```text
54
```

bleibt der Datentyp:

```python
str
```

---

# 🤔 Bedingungen

## Vergleichsoperatoren

```python
<    kleiner als
<=   kleiner oder gleich
>    größer als
>=   größer oder gleich
==   gleich
!=   ungleich
```

---

## if

```python
if alter < 18:
    print("Du bist minderjährig.")
```

---

## if / else

```python
if alter < 18:
    print("Du bist minderjährig.")
else:
    print("Du bist volljährig.")
```

---

## if / elif / else

```python
if note == 1:
    print("Sehr gut")
elif note == 2:
    print("Gut")
elif note == 3:
    print("Befriedigend")
else:
    print("Unbekannte Note")
```

💡 Merksatz:

```text
if    = wenn

elif  = sonst wenn

else  = ansonsten
```

💡 Wichtig:

```text
Bei if / elif / else wird nur
der erste zutreffende Zweig ausgeführt.
```

---

## Logische Operatoren

### and

```python
if alter >= 18 and alter <= 66:
    print("Erwachsene Person")
```

💡 Bedeutung:

```text
Beide Bedingungen müssen wahr sein.
```

---

### or

```python
if alter < 18 or alter > 67:
    print("Sondergruppe")
```

💡 Bedeutung:

```text
Mindestens eine Bedingung muss wahr sein.
```

---

### Wahrheitswerte

```text
False and False = False
True  and False = False
False and True  = False
True  and True  = True
```

```text
False or False = False
True  or False = True
False or True  = True
True  or True  = True
```

---

# 🔁 Schleifen

## while

```python
zahl = 1

while zahl <= 5:
    print(zahl)
    zahl += 1
```

Ausgabe:

```text
1
2
3
4
5
```

---

## Rückwärts zählen

```python
zahl = 5

while zahl >= 1:
    print(zahl)
    zahl -= 1
```

Ausgabe:

```text
5
4
3
2
1
```

---

## Schleife mit Bedingung

```python
zahl = 1

while zahl <= 10:
    if zahl % 2 == 0:
        print(zahl)

    zahl += 1
```

Ausgabe:

```text
2
4
6
8
10
```

---

## Schleife mit Benutzereingabe

```python
zahl = int(input("Bitte Zahl eingeben: "))

zaehler = 1

while zaehler <= zahl:
    print(zaehler)
    zaehler += 1
```

---

## Kurzschreibweisen

```python
zahl += 1
```

entspricht:

```python
zahl = zahl + 1
```

---

```python
zahl -= 1
```

entspricht:

```python
zahl = zahl - 1
```

---

## ⚠️ Endlosschleifen

Fehler:

```python
zahl = 1

while zahl <= 5:
    print(zahl)
```

💡 Problem:

```text
zahl wird nie verändert.
Die Bedingung bleibt immer True.
```

💡 Merksatz:

```text
Eine while-Schleife benötigt eine Bedingung,
die irgendwann False wird.
```

---

## for

```python
for zahl in range(1, 6):
    print(zahl)
```

Ausgabe:

```text
1
2
3
4
5
```

💡 Merksatz:

```text
Die for-Schleife eignet sich besonders,
wenn die Anzahl der Wiederholungen bekannt ist.
```

---

## range()

Aufbau:

```python
range(start, ende)
```

Beispiel:

```python
range(1, 6)
```

Ergebnis:

```text
1
2
3
4
5
```

💡 Wichtig:

```text
Der Endwert wird nicht mit ausgegeben.
```

---

## range() mit Schrittweite

Aufbau:

```python
range(start, ende, schrittweite)
```

Beispiel:

```python
for zahl in range(0, 11, 2):
    print(zahl)
```

Ausgabe:

```text
0
2
4
6
8
10
```

💡 Merksatz:

```text
Die Schrittweite bestimmt,
um wie viel der Wert erhöht wird.
```

---

## Rückwärts zählen mit for

```python
for zahl in range(10, 0, -1):
    print(zahl)
```

Ausgabe:

```text
10
9
8
7
6
5
4
3
2
1
```

💡 Merksatz:

```text
Eine negative Schrittweite zählt rückwärts.
```

---

## Vergleich: while und for

while:

```python
zahl = 1

while zahl <= 5:
    print(zahl)
    zahl += 1
```

for:

```python
for zahl in range(1, 6):
    print(zahl)
```

Ergebnis:

```text
1
2
3
4
5
```

💡 Empfehlung:

```text
Bekannte Anzahl von Wiederholungen → for

Unbekannte Anzahl von Wiederholungen → while
```

---

# 📋 Listen

## Liste erstellen

```python
staedte = ["Belm", "Osnabrück", "Bohmte"]
```

💡 Merksatz:

```text
Eine Liste speichert mehrere Werte
in einer Variablen.
```

---

## Ganze Liste ausgeben

```python
print(staedte)
```

Ausgabe:

```text
['Belm', 'Osnabrück', 'Bohmte']
```

---

## Auf Elemente zugreifen

```python
print(staedte[0])
```

Ausgabe:

```text
Belm
```

💡 Merksatz:

```text
Listen beginnen bei Index 0.
```

Beispiel:

```text
Index 0 = erstes Element
Index 1 = zweites Element
Index 2 = drittes Element
```

---

## IndexError

```python
staedte = ["Belm", "Osnabrück", "Bohmte"]

print(staedte[3])
```

Fehler:

```text
IndexError: list index out of range
```

💡 Merksatz:

```text
Der verwendete Index existiert nicht.
```

---

## Element ändern

```python
staedte = ["Belm", "Osnabrück", "Bohmte"]

staedte[2] = "Berlin"
```

Ergebnis:

```text
['Belm', 'Osnabrück', 'Berlin']
```

💡 Merksatz:

```text
liste[index] = neuer_wert

überschreibt den vorhandenen Wert.
```

---

## Elemente anhängen

```python
staedte = ["Belm", "Osnabrück"]

staedte.append("Berlin")
```

Ergebnis:

```text
['Belm', 'Osnabrück', 'Berlin']
```

💡 Merksatz:

```text
append() fügt ein Element
am Ende der Liste hinzu.
```

---

## Länge einer Liste

```python
print(len(staedte))
```

💡 Merksatz:

```text
len() liefert die Anzahl der Elemente.
```

---

## Letztes Element ermitteln

```python
staedte[len(staedte) - 1]
```

oder kürzer:

```python
staedte[-1]
```

💡 Merksatz:

```text
-1 = letztes Element
-2 = vorletztes Element
-3 = drittletztes Element
```

Beispiel:

```python
staedte = ["Belm", "Osnabrück", "Berlin", "Hamburg"]

print(staedte[-1])
```

Ausgabe:

```text
Hamburg
```

---

# ⚙️ Funktionen

Folgt später.

---

# 📂 Dateien

Folgt später.

---

# 🛟 Fehlerbehandlung

Folgt später.

---

# 📦 Module und Pakete

Folgt später.

---

# 🗄️ Datenbanken

Folgt später.

---

# 💻 Nützliche Befehle

Python-Version anzeigen:

```bash
python3 --version
```

Python-Datei ausführen:

```bash
python3 dateiname.py
```

---

# 🚀 Aktueller Lernstand

✅ Variablen

✅ Datentypen

✅ Rechnen

✅ Datentyp-Umwandlung

✅ Benutzereingaben

✅ Bedingungen mit `if`

✅ Bedingungen mit `else`

✅ Bedingungen mit `elif`

✅ Logische Operatoren (`and`, `or`)

✅ while-Schleifen

✅ Endlosschleifen

✅ Schleifen mit Bedingungen

✅ Schleifen mit Benutzereingaben

✅ for-Schleifen

✅ range()

✅ Schrittweiten

✅ Rückwärts zählen mit for

✅ Listen erstellen

✅ Auf Listenelemente zugreifen

✅ Werte ändern

✅ append()

✅ len()

✅ Negative Indizes

🔜 Als Nächstes: Listen und for-Schleifen kombinieren