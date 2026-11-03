# 🐍 python-lernen

> **Mein persönliches Lern-Repository für Python.**  
> Dokumentation, Übungen, Nachschlagewerk und Praxisprojekte zur systematischen Erarbeitung von Python – von den Grundlagen bis zur Automatisierung.

---

## 📌 Schnellzugriff & Dokumentation

- 📖 **[Lernjournal](lernjournal/LERNJOURNAL.md)** – Chronologische Dokumentation aller Lektionen (01–24), Übungen und Prüfungen.
- 📚 **[Nachschlagewerk](nachschlagewerk/PYTHON_NACHSCHLAGEWERK.md)** – Kompakte Syntax-Übersicht, Code-Beispiele, `__pycache__`-Erklärung und Merksätze.

---

## 📈 Aktueller Lernstatus

- **Lernstand:** Lektion 24 – Modulare Software-Architektur, Rechnungs-Parsing & Oracle `INSERT` (`RECHNUNGS_KOPF`) ✅
- **Letzter Meilenstein:** Erfolgreiche Modulaufteilung (`pdf_utils`, `get_vendor`, `get_invoice_details`, `datenbank`), Abfrage der `KREDITOREN_ID` und Absicherung des Oracle `INSERT` mit `oracledb.IntegrityError`.
- **Zwischenprüfung 01:** ✅ Bestanden (9 / 10 Punkte)
- **Gesamttest (Lektion 01–21):** ✅ Bestanden (10 / 12 Punkte - 83 %)

---

## 🎯 Schwerpunkte & Lernziele

- **Python-Grundlagen:** Variablen, Datentypen, Bedingungen (`if/elif/else`), Schleifen (`while`/`for`), Listen
- **Funktionen & Modularisierung:** `def`, Parameter-Standardwerte, `return`, Variable-Unpacking, Modul-Imports
- **Datenverarbeitung & Dateizugriffe:** Dateien lesen, schreiben, zeilenweise parsen (`open()`, `.strip()`, `.split()`)
- **Fehlerbehandlung & Logging:** Robuster Code mit `try / except`, Fehlerprotokollierung in `import_fehler.log`
- **Praxisprojekte & Automatisierung:**
  - PDF-Rechnungen und EGN-Dokumente automatisiert auswerten (`pypdf`)
  - Oracle-Datenbankanbindungen & automatisierte Importprozesse (`oracledb`)

---

## 📂 Projektstruktur

```text
python-lernen
│
├── README.md                          ← Hauptübersicht & Einstieg
│
├── lernjournal
│   └── LERNJOURNAL.md                 ← Chronologisches Lernjournal
│
├── nachschlagewerk
│   └── PYTHON_NACHSCHLAGEWERK.md      ← Syntax & Nachschlagewerk (inkl. __pycache__)
│
├── lektionen                          ← Code-Beispiele nach Lektionen
│   ├── lektion01_variablen
│   ├── lektion02_bedingungen
│   ├── lektion03_schleifen
│   ├── ...
│   └── lektion24_modulares_parsing    ← Modulares Rechnungs-Parsing & Oracle INSERT
│
├── uebungen                           ← Eigene Übungsaufgaben & Lösungen
│
└── projekte                           ← Praxisanwendungen & Automatisierungen
    ├── pdf_import
    └── oracle
```

---

## 🛠️ Ausführung & Anwendung

```bash
# Hauptprogramm für Rechnungseingangs-Verarbeitung ausführen
python3 main.py
```

---

## 🤝 Lernmethode & Protokoll

Dieses Repository wird nach einem festen **1-zu-1-Lernprinzip** gepflegt:
- **Ein Thema nach dem anderen:** Fokus auf schrittweises Verstehen ohne Überforderung.
- **Direkte Dokumentation:** Abgeschlossene Lektionen werden unmittelbar ins Lernjournal und Nachschlagewerk überführt.
- **Praxisorientiert:** Jede Lektion schließt mit einer konkreten Übung ab.
