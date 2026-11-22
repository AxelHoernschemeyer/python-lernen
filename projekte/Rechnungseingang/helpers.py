""" Hilfssdatei für alle Projekte. """
#   =========================================
#   Erstellt von Axel Hörnschemeyer
#   Stand: 1.00
#   eMail: axel.hoernschemeyer@googlemail.com
#   =========================================

# Hilfsfunktionen für Datumsformatierungen und Text-Konvertierungen

import calendar

# Zuordnungstabelle für deutsche Monatsnamen
MONATE = {
    "Jannuar": "01", "Februar": "02", "März": "03", "April": "04", "Mai": "05",
    "Juni": "06", "Juli": "07", "August": "08", "September": "09", "Oktober": "10",
    "November": "11", "Dezember": "12",
    "Jan": "01", "Feb": "02", "Mär": "03", "Apr": "04", 
    "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Okt": "10",
    "Nov": "11", "Dez": "12"
    }

def monat_jahr_zu_datum(monat_jahr_text, standard_tag="01"):
    """ Wandelt z.B. 'November 2026' in 01.11.2026 um """
    teile = monat_jahr_text.strip().split() # -> ['November','2026']
    if len(teile) >= 2 :
        monat_name = teile[0].capitalize()
        monat_zahl = MONATE.get(monat_name, "01")
        jahr = teile[1]
        return f"{standard_tag}.{monat_zahl}.{jahr}"
    return None

def monat_jahr_zu_zeitraum(monat_jahr_text):
    """ Ermittelt den ersten und den letzten Tage des Monats aus."""
    teile = monat_jahr_text.strip().split() # -> ['November', '2026'] <- eine Liste
    if len(teile) >= 2:
        monat_name = teile[0].capitalize()
        monat_zahl = int(MONATE.get(monat_name,1))
        jahr       = int(teile[1])

        # Anzahl der Tage im Monat ermitteln (z.B. 30 für November)
        _, anzahl_tage = calendar.monthrange(jahr, monat_zahl)

        # Ruft die Funktion monat_jahr_zu_datum auf für 1 und den
        # letzten Tag des Monats.
        von_datum = monat_jahr_zu_datum(monat_jahr_text)
        bis_datum = monat_jahr_zu_datum(monat_jahr_text, anzahl_tage)
        return f"{von_datum}.{bis_datum}.{jahr}"
    return None
