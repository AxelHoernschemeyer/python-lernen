# 🐍 Python Lernjournal

> Repository: `python-lernen`
>
> 🎯 Hauptziel:
>
> Python von Grund auf lernen und sicher anwenden können.
>
> 🚀 Langfristige Schwerpunkte:
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
> 🛠️ Praxisprojekte:
>
> - PDF-Rechnungen auswerten
> - Daten validieren
> - Fehler protokollieren
> - Datenbanken anbinden
> - Eigene Python-Anwendungen entwickeln

---

# 📅 17.10.2026

## ✅ Lektion 01 – Variablen und Ausgaben

### 📚 Gelernt

- Variablen anlegen
- Werte zuweisen
- Texte und Zahlen ausgeben
- `print()` verwenden
- Variablen in Ausgaben verwenden

### 💻 Übungen

- Persönliche Daten in Variablen gespeichert
- Eigene Ausgaben mit `print()` erstellt

### 💡 Erkenntnisse

✅ Variablen müssen nicht deklariert werden.

✅ Python erkennt den Datentyp automatisch.

✅ Mehrere Werte können mit `print()` ausgegeben werden.

### 🎯 Status

✅ Verstanden

---

## ✅ Lektion 02 – Datentypen

### 📚 Gelernt

| Datentyp | Beschreibung | Beispiel |
|-----------|-----------|-----------|
| `str` | Text | `"Axel"` |
| `int` | Ganze Zahl | `54` |
| `float` | Kommazahl | `1.82` |
| `bool` | Wahr/Falsch | `True` |

### 💻 Übungen

- Datentypen angelegt
- Datentypen mit `type()` geprüft

### 💡 Erkenntnisse

✅ Python unterscheidet zwischen Text und Zahlen.

✅ Der gleiche Inhalt kann unterschiedliche Datentypen besitzen.

Beispiele:

```text
54   → int
"54" → str
1.82 → float
True → bool
```

### 🎯 Status

✅ Verstanden

---

## ✅ Lektion 03 – Rechnen mit Zahlen

### 📚 Gelernt

- Addition (`+`)
- Subtraktion (`-`)
- Multiplikation (`*`)
- Division (`/`)
- Ganzzahldivision (`//`)
- Modulo (`%`)

### 💻 Übungen

- Rechnen mit Variablen
- Ganzzahldivision
- Modulo

### 💡 Erkenntnisse

✅ Modulo liefert den Rest einer Division.

Beispiel:

```text
20 % 3 = 2
```

✅ Ganzzahldivision entfernt Nachkommastellen.

Beispiel:

```text
20 // 3 = 6
```

✅ Strings können mit einer Zahl multipliziert werden.

Beispiel:

```python
"Axel" * 5
```

Ergebnis:

```text
AxelAxelAxelAxelAxel
```

✅ Eine Addition von String und Integer führt zu einem Fehler.

Beispiel:

```python
"5" + 1
```

Ergebnis:

```text
TypeError
```

### 🎯 Status

✅ Verstanden

---

## ✅ Lektion 04 – Benutzereingaben

### 📚 Gelernt

- Benutzereingaben mit `input()`
- Ausgaben von Benutzereingaben
- Einfache Interaktion mit dem Benutzer

### 💻 Übungen

- Vorname abfragen
- Alter abfragen
- Wohnort abfragen

### 💡 Erkenntnisse

✅ `input()` liefert immer einen String (`str`) zurück.

Folgende Eingaben liefern alle einen String:

```text
54
54.3
Axel
```

✅ Auch Zahlen bleiben zunächst Text.

### 🎯 Status

✅ Verstanden

---

## ✅ Lektion 05 – Datentypen umwandeln

### 📚 Gelernt

- Umwandlung mit `int()`
- Umwandlung mit `float()`
- Unterschied zwischen `int()` und `round()`

### 💻 Übungen

- Benutzereingaben in Zahlen umwandeln
- Zahlen addieren

### 💡 Erkenntnisse

✅ `int()` wandelt einen String in eine Ganzzahl um.

✅ `float()` wandelt einen String in eine Kommazahl um.

✅ `int()` schneidet Nachkommastellen ab.

✅ `round()` rundet eine Zahl.

✅ Nicht jeder String kann in einen Integer umgewandelt werden.

### 🎯 Status

✅ Verstanden

---

## ✅ Lektion 06 – Bedingungen mit if

### 📚 Gelernt

- Vergleichsoperatoren
- `if`
- `else`

### 💻 Übungen

- Volljährigkeit prüfen
- Minderjährigkeit prüfen

### 💡 Erkenntnisse

✅ Bedingungen liefern entweder `True` oder `False`.

✅ Mit `if` werden Entscheidungen getroffen.

✅ Mit `else` wird die Alternative ausgeführt.

✅ Der Unterschied zwischen `=` und `==` wurde verstanden.

### 🎯 Status

✅ Verstanden

---

## ✅ Lektion 07 – Bedingungen mit elif

### 📚 Gelernt

- `elif`
- Mehrere Bedingungen prüfen
- Logische Operatoren `and` und `or`

### 💻 Übungen

- Schulnoten auswerten
- Altersgruppen bestimmen
- Mehrere Bedingungen in einer Abfrage verarbeiten

### 💡 Erkenntnisse

✅ Mit `elif` können mehrere Bedingungen nacheinander geprüft werden.

✅ Python arbeitet bei `if / elif / else` von oben nach unten.

✅ Nur der erste zutreffende Zweig wird ausgeführt.

✅ `and` bedeutet, dass beide Bedingungen wahr sein müssen.

✅ `or` bedeutet, dass mindestens eine Bedingung wahr sein muss.

### 🎯 Status

✅ Verstanden

---

## 📝 Zwischenprüfung 01

### 📚 Themen

- Variablen
- Datentypen
- Rechenoperatoren
- Benutzereingaben
- Datentypumwandlung
- Bedingungen
- Vergleichsoperatoren
- `and`
- `or`

### 🏆 Ergebnis

**9 von 10 Punkten**

### 💡 Erkenntnisse

✅ Datentypen sicher verstanden

✅ Rechenoperatoren sicher verstanden

✅ Bedingungen sicher verstanden

✅ Unterschied zwischen `=` und `==` verstanden

⚠️ Aufgabenstellungen vollständig lesen

### 🎯 Status

✅ Bestanden

---

## ✅ Lektion 08 – Schleifen mit while

### 📚 Gelernt

- `while`
- Zählvariablen
- Endlosschleifen
- Schleifen mit Bedingungen kombinieren

### 💻 Übungen

- Zahlen von 1 bis 5 ausgeben
- Rückwärts zählen
- Quadratzahlen berechnen
- Gerade und ungerade Zahlen erkennen
- Benutzereingaben mit Schleifen kombinieren

### 💡 Erkenntnisse

✅ Eine `while`-Schleife wird ausgeführt, solange die Bedingung `True` ist.

✅ Der Schleifenzähler muss verändert werden.

✅ Schleifen können mit Bedingungen kombiniert werden.

✅ Benutzereingaben können als Obergrenze einer Schleife verwendet werden.

✅ `+= 1` erhöht eine Variable um 1.

### 🎯 Status

✅ Verstanden

---

## ✅ Lektion 09 – for-Schleifen

### 📚 Gelernt

- `for`
- `range()`
- Schrittweiten
- Rückwärts zählen mit negativer Schrittweite

### 💻 Übungen

- Zahlen von 1 bis 10 ausgeben
- Gerade Zahlen mit Schrittweite 2 ausgeben
- Rückwärts von 10 bis 1 zählen

### 💡 Erkenntnisse

✅ Die `for`-Schleife eignet sich besonders, wenn die Anzahl der Wiederholungen bekannt ist.

✅ `range(start, ende)` erzeugt einen Zahlenbereich.

✅ Das Ende wird bei `range()` nicht mit ausgegeben.

✅ Mit einer Schrittweite können Zahlen übersprungen werden.

✅ Mit einer negativen Schrittweite kann rückwärts gezählt werden.

### 🎯 Status

✅ Verstanden

---

## ✅ Lektion 10 – Listen

### 📚 Gelernt

- Listen erstellen
- Elemente über den Index lesen
- Elemente ändern
- Elemente hinzufügen
- Listenlänge bestimmen
- Negative Indizes verwenden

### 💻 Übungen

- Liste mit Städten erstellt
- Auf einzelne Listenelemente zugegriffen
- Elemente geändert
- Neue Elemente mit `append()` hinzugefügt
- Listenlänge mit `len()` bestimmt
- Letztes Element einer Liste ermittelt

### 💡 Erkenntnisse

✅ Eine Liste kann mehrere Werte in einer Variablen speichern.

Beispiel:

```python
staedte = ["Belm", "Osnabrück", "Berlin"]
```

✅ Listen beginnen bei Index `0`.

Beispiel:

```text
0 = Belm
1 = Osnabrück
2 = Berlin
```

✅ Ein ungültiger Index führt zu:

```text
IndexError: list index out of range
```

✅ Mit

```python
liste[index] = wert
```

kann ein vorhandener Wert geändert werden.

✅ Mit

```python
append()
```

wird ein neues Element am Ende der Liste angefügt.

✅ Mit

```python
len()
```

kann die Anzahl der Elemente ermittelt werden.

✅ Negative Indizes zählen vom Ende der Liste.

Beispiel:

```text
-1 = letztes Element
-2 = vorletztes Element
```

### 🎯 Status

✅ Verstanden

---

# 📚 Zusammenfassung des aktuellen Lernstands

Bisher sicher verstanden:

✅ Variablen

✅ Ausgaben mit `print()`

✅ Datentypen

✅ Datentypen prüfen mit `type()`

✅ Rechenoperatoren

✅ Ganzzahldivision

✅ Modulo

✅ Benutzereingaben

✅ Datentypen umwandeln

✅ Bedingungen mit `if`

✅ Bedingungen mit `else`

✅ Bedingungen mit `elif`

✅ Logische Operatoren (`and`, `or`)

✅ while-Schleifen

✅ Endlosschleifen erkennen

✅ Schleifen mit Bedingungen kombinieren

✅ for-Schleifen

✅ range()

✅ Schrittweiten

✅ Rückwärts zählen mit range()

✅ Listen

✅ Listenindizes

✅ append()

✅ len()

✅ Negative Indizes

---

# 🎯 Nächste Lektionen

🔜 Schleifen mit Listen

🔜 Verschachtelte Schleifen

🔜 Erste kleine Projekte

🔜 Listen erweitern

🔜 Zwischenprüfung 02

---

# 🚀 Persönliches Fazit

Die Grundlagen von Python sind gelegt.

Der Umgang mit Variablen, Datentypen, Rechenoperatoren, Benutzereingaben, Bedingungen, Schleifen und einfachen Listen ist verstanden.

Die nächsten Schritte konzentrieren sich auf die Verarbeitung mehrerer Werte mit Listen und Schleifen.

---

# 📍 Aktueller Stand

✅ Lektion 01 abgeschlossen

✅ Lektion 02 abgeschlossen

✅ Lektion 03 abgeschlossen

✅ Lektion 04 abgeschlossen

✅ Lektion 05 abgeschlossen

✅ Lektion 06 abgeschlossen

✅ Lektion 07 abgeschlossen

✅ Zwischenprüfung 01 bestanden

✅ Lektion 08 abgeschlossen

✅ Lektion 09 abgeschlossen

✅ Lektion 10 abgeschlossen