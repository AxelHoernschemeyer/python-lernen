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

Beispiele:

```python
int(54.9)
```

Ergebnis:

```text
54
```

```python
round(54.9)
```

Ergebnis:

```text
55
```

✅ Nicht jeder String kann in einen Integer umgewandelt werden.

Beispiel:

```python
int("Axel")
```

Ergebnis:

```text
ValueError
```

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

Verwendete Vergleichsoperatoren:

```python
<    kleiner als
<=   kleiner oder gleich
>    größer als
>=   größer oder gleich
==   gleich
!=   ungleich
```

Beispiel:

```python
alter = 18
```

führt bei

```python
if alter < 18:
```

zu:

```text
False
```

und damit zur Ausführung von `else`.

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

---

# 🎯 Nächste Lektionen

🔜 `elif`

🔜 Verschachtelte Bedingungen

🔜 Logische Operatoren (`and`, `or`, `not`)

🔜 Erste kleine Programme

🔜 Erste Zwischenprüfung

---

# 🚀 Persönliches Fazit

Die Grundlagen von Python sind gelegt.

Der Umgang mit Variablen, Datentypen, Rechenoperatoren, Benutzereingaben und einfachen Bedingungen ist verstanden.

Die nächsten Schritte konzentrieren sich auf Entscheidungslogik und den Aufbau kleiner eigenständiger Programme.

---

📍 Aktueller Stand:

✅ Lektion 01 abgeschlossen

✅ Lektion 02 abgeschlossen

✅ Lektion 03 abgeschlossen

✅ Lektion 04 abgeschlossen

✅ Lektion 05 abgeschlossen

✅ Lektion 06 abgeschlossen