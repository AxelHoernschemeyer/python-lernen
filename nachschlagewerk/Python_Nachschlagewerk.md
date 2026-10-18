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

💡 Merksatz:

```text
Modulo liefert den Rest einer Division.
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

💡 Merksätze:

```text
if   = wenn

else = ansonsten
```

Beispiel:

```python
alter = 18

if alter < 18:
    print("minderjährig")
else:
    print("volljährig")
```

Ausgabe:

```text
volljährig
```

---

# 🔁 Schleifen

Folgt später.

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

✅ Bedingungen mit `if` und `else`

🔜 Als Nächstes: `elif`
