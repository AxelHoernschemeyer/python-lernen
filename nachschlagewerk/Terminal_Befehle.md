# 🖥️ Terminal & CLI Nachschlagewerk

> **Spickzettel für nützliche Terminal-Befehle (macOS & Python-Umgebung)**  
> *Ziel:* Schnelle Referenz für Paketinstallationen, Skriptausführungen und Terminal-Navigation.

---

## 📌 Inhaltsverzeichnis

- [1. Python-Paketverwaltung (`pip`)](#1-python-paketverwaltung-pip)
- [2. Python-Skripte ausführen](#2-python-skripte-ausführen)
- [3. Grundlegende Navigation im macOS Terminal](#3-grundlegende-navigation-im-macos-terminal)

---

## 1. Python-Paketverwaltung (`pip`)

| Befehl | Beschreibung | Beispiel |
| :--- | :--- | :--- |
| `python3 -m pip install <paket>` | Installiert ein externes Python-Paket | `python3 -m pip install pypdf` |
| `python3 -m pip install --upgrade <paket>` | Aktualisiert ein installiertes Paket | `python3 -m pip install --upgrade oracledb` |
| `python3 -m pip list` | Listet alle installierten Pakete auf | `python3 -m pip list` |
| `pip3 install --upgrade pip` | Aktualisiert den Paketmanager `pip` selbst | `pip3 install --upgrade pip` |

> 💡 **Tipp:** Verwende auf dem Mac bevorzugt `python3 -m pip install ...`, da so sichergestellt wird, dass das Paket exakt in der aktiven Python-3-Umgebung installiert wird.

---

## 2. Python-Skripte ausführen

| Befehl | Beschreibung | Beispiel |
| :--- | :--- | :--- |
| `python3 <skriptname.py>` | Führt ein Python-Skript aus | `python3 main.py` |
| `python3 -m <modulname>` | Führt ein Modul direkt aus | `python3 -m pip list` |

---

## 3. Grundlegende Navigation im macOS Terminal

| Befehl | Bedeutung / Funktion |
| :--- | :--- |
| `pwd` | Zeigt den aktuellen Ordnerpfad an (*Print Working Directory*) |
| `ls -la` | Listet alle Dateien und Ordner detailliert auf |
| `cd <ordnername>` | Wechselt in einen Unterordner |
| `cd ..` | Springt einen Ordner höher |
| `clear` | Leert die Bildschirmausgabe des Terminals |
