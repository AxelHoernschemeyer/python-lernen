import os
import requests

# macOS Downloads-Ordner automatisch ermitteln
DOWNLOADS_ORDNER = os.path.join(os.path.expanduser("~"), "Downloads")

# Saison 2026/2027
saison = "2026" 

spieltag = input("Für welchen Spieltag möchtest du die Datei erstellen (z.B. 1, 15, 34)? ")

# 1. Abfrage, ob Tipps eingetragen werden sollen
tipp_frage = input("Möchtest du für diesen Spieltag Tipps erfassen? (j/n): ").strip().lower()
tipp_erfassen = tipp_frage in ['j', 'ja', 'y', 'yes']

# Daten von der OpenLigaDB API abrufen
url = f"https://api.openligadb.de/getmatchdata/bl1/{saison}/{spieltag}"
response = requests.get(url)

if response.status_code != 200:
    print(f"Fehler beim Abrufen der Daten! Statuscode: {response.status_code}")
    exit()

matches = response.json()

if not matches:
    print(f"Keine Spiele für Spieltag {spieltag} in der Saison {saison} gefunden.")
    exit()

dateiname = f"spieltag_{spieltag}.txt"
vollstaendiger_pfad = os.path.join(DOWNLOADS_ORDNER, dateiname)

if tipp_erfassen:
    print(f"\n--- Eingabe der Tipps für Spieltag {spieltag} ---")

with open(vollstaendiger_pfad, "w", encoding="utf-8") as f:
    for match in matches:
        team1 = match['team1']['teamName']
        team2 = match['team2']['teamName']
        
        # Prüfen, ob das Spiel beendet ist und Ergebnisse vorliegen
        is_finished = match.get('matchIsFinished', False)
        results = match.get('matchResults', [])
        
        if is_finished and results:
            tore1 = results[-1].get('pointsTeam1', 0)
            tore2 = results[-1].get('pointsTeam2', 0)
            ergebnis = f"{tore1}:{tore2}"
        else:
            ergebnis = ""  # Bleibt komplett leer, wenn noch kein Ergebnis vorliegt

        # Tipp ermitteln (nur wenn gewollt)
        tipp = ""
        if tipp_erfassen:
            eingabe = input(f"Dein Tipp für {team1} vs. {team2} (oder einfach Enter für leer): ").strip()
            if eingabe:
                tipp = eingabe

        # Zeile aufbauen: Spieltag;Heimmannschaft;Gastmannschaft;Ergebnis;Tipp
        zeile = f"{spieltag};{team1};{team2};{ergebnis};{tipp}\n"
        f.write(zeile)

print(f"\n✅ Erfolgreich! Die Datei wurde in deinen Downloads gespeichert:\n{vollstaendiger_pfad}")