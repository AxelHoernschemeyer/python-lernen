""" Hauptprogramm für die Rechnungseingang-Verarbeitung """
#   =========================================
#   Erstellt von Axel Hörnschemeyer
#   Stand: 1.00
#   eMail: axel.hoernschemeyer@googlemail.com
#   =========================================

from pathlib import Path
import shutil
import datenbank as db
import pdf_utils as pdf
import get_vendor
import get_invoice_details as inv_details

PWD = input("Bitte geben Sie das Kennwort für die Datenbank ein: ")

# Pfade sauber als Path-Objekte anlegen
BASE_DIR = Path("/Users/axelhoernschemeyer/Downloads/Oracle-Projekte/Mobilfunkvertragsauswertung")
INBOX = BASE_DIR / "Inbox"
ARCHIVE = BASE_DIR / "Archiv"

# Durchsucht das Inbox-Verzeichnis nach PDF-Dateien und verarbeitet jede Datei einzeln
for pdf_file in INBOX.glob("*.pdf"):
    filename = pdf_file.name  # z. B. "B949807855_RG.pdf"
    filepath = str(pdf_file)  # Vollständiger Dateipfad

    print(f"📄 Verarbeite Datei: {filename}")

    # 1. PDF-Text EINMALIG einlesen
    pdf_text = pdf.lese_pdf_datei(filepath)

    # 2. Aussteller erkennen
    aussteller = get_vendor.erkenne_aussteller(pdf_text, db.get_all_vendor(PWD))

    # Prüfen, ob ein Aussteller gefunden wurde
    if aussteller is None or aussteller == "Kreditor nicht gefunden":
        continue  # Springt sofort zur nächsten Datei!

    # 3. Details auslesen
    details = inv_details.erkenne_rechnungsdetails(pdf_text, aussteller)

    # 4. IDs aus der Datenbank abrufen
    tarif = details.get("Tarif", "")
    kreditor_id = db.get_vendor_id(aussteller, PWD)
    tarif_id = db.get_tarif_id(tarif, PWD)

    # 5. Ausgelesene Daten in die Datenbank speichern (NUR EINMAL)
    db.speichere_rechnung(kreditor_id, tarif_id, filename, details, PWD)

    # 6. Verschieben der Datei in das Archivverzeichnis
    shutil.move(pdf_file, ARCHIVE / filename)
    print(f"📦 {filename} wurde erfolgreich ins Archiv verschoben.\n")
