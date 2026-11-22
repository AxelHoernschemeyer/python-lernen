""" Hilfsfunktionen für die PDF-Verarbeitung """
#   =========================================
#   Erstellt von Axel Hörnschemeyer
#   Stand: 1.00
#   eMail: axel.hoernschemeyer@googlemail.com
#   =========================================

import logging
from pypdf import PdfReader

# Schaltet alle Warn- und Info-Meldungen von pypdf stumm:
logging.getLogger("pypdf").setLevel(logging.ERROR)

def lese_pdf_datei(file_path):
    """ Liest den Inhalt einer PDF-Datei ein und gibt ihn als Liste von Textzeilen zurück. """
    reader = PdfReader(file_path)
    inhalt_pdf = (reader.get_page(0).extract_text() or "").split("\n")
    return inhalt_pdf
