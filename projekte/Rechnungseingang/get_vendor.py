""" Hier werden die Kreditoren aus dem aktuellen Rechnungsdokuments ausgelesen """
#   =========================================
#   Erstellt von Axel Hörnschemeyer
#   Stand: 1.00
#   eMail: axel.hoernschemeyer@googlemail.com
#   =========================================

def erkenne_aussteller(text_inhalt_pdf, kreditoren_liste):
    """ Ermittelt den Kreditor anhand des Textes auf der ersten Seite. """
    for kreditor in kreditoren_liste:
        for zeile in text_inhalt_pdf:
            if kreditor in zeile:
                return kreditor
    return "Kreditor nicht gefunden"
