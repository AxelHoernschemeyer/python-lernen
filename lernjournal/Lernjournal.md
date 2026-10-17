# 🐍 Python Lernjournal

> Repository: `python-lernen`
>
> Hauptziel:
>
> Python von Grund auf lernen und sicher anwenden können.
>
> Langfristige Schwerpunkte:
>
> - Python-Grundlagen
> - Datentypen und Datenstrukturen
> - Bedingungen und Schleifen
> - Funktionen und Module
> - Fehlerbehandlung
> - Dateien lesen und schreiben
> - Objektorientierte Programmierung (OOP)
> - Automatisierung
> - Datenverarbeitung
> - PDF-Auswertung
> - Datenbankanbindungen
>
> Praxisprojekte:
>
> - PDF-Rechnungen auswerten
> - Daten validieren
> - Fehler protokollieren
> - Datenbanken anbinden
> - Eigene Python-Anwendungen entwickeln

---

# 📅 17.10.2026

## ✅ Lektion 01 – Variablen und Ausgaben

### Gelernt

- Variablen anlegen
- Werte zuweisen
- Texte und Zahlen ausgeben
- `print()` verwenden
- Variablen in Ausgaben verwenden

### Übungen

```python
vorname = "Axel"
nachname = "Hörnschemeyer"
alter = 54
wohnort = "Belm-Vehrte"

print(
    "Hallo Python, mein Name ist",
    vorname,
    nachname,
    "und ich bin",
    alter,
    "Jahre alt. Ich wohne in",
    wohnort
)
```

### Erkenntnisse

- Variablen müssen nicht deklariert werden.
- Python erkennt den Datentyp automatisch.
- Mehrere Werte können mit `print()` ausgegeben werden.

### Status

✅ Verstanden

---

## ✅ Lektion 02 – Datentypen

### Gelernt

| Datentyp | Beschreibung | Beispiel |
|-----------|-----------|-----------|
| `str` | Text | `"Axel"` |
| `int` | Ganze Zahl | `54` |
| `float` | Kommazahl | `1.82` |
| `bool` | Wahr/Falsch | `True` |

### Übungen

```python
vorname = "Axel"
alter = 54
groesse = 1.82
verheiratet = True

print(type(vorname))
print(type(alter))
print(type(groesse))
print(type(verheiratet))
```

### Erkenntnisse

```python
54
```

ist ein Integer:

```python
int
```

---

```python
"54"
```

ist ein String:

```python
str
```

---

```python
1.82
```

ist ein Float:

```python
float
```

---

```python
True
False
```

sind Boolean-Werte:

```python
bool
```

### Status

✅ Verstanden

---

## ✅ Lektion 03 – Rechnen mit Zahlen

### Gelernt

```python
+   # Addition
-   # Subtraktion
*   # Multiplikation
/   # Division
//  # Ganzzahldivision
%   # Modulo
```

### Übungen

```python
zahl1 = 20
zahl2 = 5

print("Addition:", zahl1 + zahl2)
print("Subtraktion:", zahl1 - zahl2)
print("Multiplikation:", zahl1 * zahl2)
print("Division:", zahl1 / zahl2)
```

---

```python
zahl1 = 20
zahl2 = 6

print("Ganzzahldivision:", zahl1 // zahl2)
print("Modulo:", zahl1 % zahl2)
```

### Erkenntnisse

```python
20 // 3
```

Ergebnis:

```python
6
```

Die Nachkommastellen werden entfernt.

---

```python
20 % 3
```

Ergebnis:

```python
2
```

Modulo liefert den Rest einer Division.

---

Interessante Beobachtung:

```python
print("Axel" * 5)
```

Ergebnis:

```text
AxelAxelAxelAxelAxel
```

Strings können mit einer Ganzzahl multipliziert werden.

---

```python
print("5" * 3)
```

Ergebnis:

```text
555
```

Auch Zahlen in Anführungszeichen gelten als Text (`str`) und werden wiederholt.

### Status

✅ Verstanden

---

# 📚 Zusammenfassung des aktuellen Lernstands

Bisher sicher verstanden:

- Variablen
- Ausgaben mit `print()`
- Datentypen
- Datentypen prüfen mit `type()`
- Grundlegende Rechenoperatoren
- Ganzzahldivision
- Modulo

---

# 🎯 Nächste Lektionen

- Benutzereingaben mit `input()`
- Umwandlung von Datentypen (`int()`, `str()`, `float()`)
- Bedingungen mit `if`
- Vergleiche (`==`, `!=`, `<`, `>`)
- Erste kleine Programme

---

# 🚀 Persönliches Fazit

Die Grundlagen von Python sind gelegt.

Der Umgang mit Variablen, Datentypen und Rechenoperatoren ist verstanden. Die nächsten Schritte sind Benutzereingaben und erste Entscheidungen mit `if`-Abfragen.

Stand: Lektion 01 bis 03 abgeschlossen ✅