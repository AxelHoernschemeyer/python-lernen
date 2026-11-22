""" Funktionen zur Extraktion von Rechnungsdetails aus PDF-Dateien """
#   =========================================
#   Erstellt von Axel Hörnschemeyer
#   Stand: 1.00
#   eMail: axel.hoernschemeyer@googlemail.com
#   =========================================

import helpers

def erkenne_rechnungsdetails(text_inhalt_pdf,aussteller):
    """ Ermittelt die Rechnungsdetails anhand des Textes auf der ersten Seite. """
    details = {}
    match aussteller:
        case "Drillisch Online GmbH":
            for index, zeile in enumerate(text_inhalt_pdf):
                if "Kunden Nr." in zeile:
                    details["Kunden-Nr."]       = text_inhalt_pdf[index + 1].strip()
                elif "Datum" in zeile:
                    details["Rechnungsdatum"]   = text_inhalt_pdf[index + 1].strip()
                elif "Rufnummer" in zeile:
                    details["Rufnummer"]        = text_inhalt_pdf[index + 1].strip()
                elif "Tarif" == zeile:
                    details["Tarif"]            = text_inhalt_pdf[index + 1].strip()
                elif "Rechnung" == zeile:
                    details["Rechnungsnummer"]  = text_inhalt_pdf[index + 1].strip()
                elif "USt-Satz" in zeile:
                    details["USt-Satz"]         = text_inhalt_pdf[index + 1].split(" ")[0]
                elif "in Höhe von" in zeile:
                    # 1. Rechten Teil nach "in Höhe von " greifen
                    rechter_teil = zeile.split("in Höhe von ")[1]
                    # 2. Am ersten Leerzeichen trennen und das erste Wort (Index 0) nehmen
                    betrag = rechter_teil.split(" ")[0]
                    details["Rechnungsbetrag"] = round(float(betrag.replace(',', '.')), 2)
                elif "Für den Zeitraum" in zeile:
                    # 1. Text nach "Für den Zeitraum " nehmen ("01.09.-30.09.2026 ...")
                    rechter_teil = zeile.split("Für den Zeitraum ")[1]
                    # 2. Am ersten Leerzeichen trennen, Index [0] nehmen und säubern
                    details["Zeitraum"] = rechter_teil.split(" ")[0].strip()
                elif "Summe " in zeile:
                    # .split() ohne Arg fasst alle Leerzeichen zusammen!
                    teile = zeile.split()
                    if len(teile) >= 2:
                        details["NettoRGbetrag"] = round(float(teile[1].replace(',', '.')), 2)
                        details["USt-Betrag"] = round(float(teile[3].replace(',', '.')), 2)
                elif zeile.startswith("Guten Tag "):
                    # Entfernt den Text "Guten Tag " und das Komma am Ende, für den Empfänger
                    details["Empfänger"] = zeile.replace("Guten Tag ", "").rstrip(",").strip()
        case "Vodafone GmbH":
            for index, zeile in enumerate(text_inhalt_pdf):
                if "Kundennummer" in zeile:
                    details["Kunden-Nr."] = zeile.split("Kundennummer ")[1]
                elif "Datum" in zeile:
                    datum = zeile.split()
                    if len(datum) >= 3 :
                        tag = datum[1].replace('.','')
                        if len(tag) == 1 :
                            tag = ("0" + tag)
                        details["Rechnungsdatum"] = \
                            helpers.monat_jahr_zu_datum(datum[2]+ " " + \
                                                        datum[3],tag)
                elif "Rechnungsnummer" == zeile:
                    details["Rechnungsnummer"]  = zeile.split("Rechnungsnummer ")[1]
                elif "'"'MwSt. ('"'" in zeile:
                    details["Steuer"]  = zeile.split("MwSt. ( ")[1]
                elif "Rechnungsbetrag (brutto, inkl. MwSt.)" in zeile:
                    # Teilt die Zeile in einzelne Werte und erstellt eine Liste mit , getrennt.
                    # Aus der Liste wird dann der vorletzte Wert genommen.
                    # -1 wäre der letzt Wert der Liste
                    betrag = zeile.split()[-2]
                    details["Rechnungsbetrag"] = round(float(betrag.replace(',', '.')), 2)
            # elif "Rechnungsbetrag (netto, ohne)" in zeile:
            #     nbetrag = zeile.split()[-2]
            #     details["NettoRGbetrag"] = round(float(nbetrag.replace(',', '.')), 2)

            # elif "Ihre Rechnung für" in zeile:
            #     # 1. Text nach "Ihre Rechnung für" nehmen ("November 2026 ...")
            #     monat_jahr = zeile.split("Ihre Rechnung für ")[1].strip()
            #     # Wandelt es um in 01.11.2026
            #     details["Zeitraum_Von"] = helpers.monat_jahr_zu_zeitraum(monat_jahr)[0].strip()
            #     details["Zeitraum_Bis"] = helpers.monat_jahr_zu_zeitraum(monat_jahr)[1].strip()
                elif "Herr" in zeile:
                    details["Empfänger"] = text_inhalt_pdf[index + 1].strip()
    return details

# details["Empfänger"] = text_inhalt_pdf[9].strip()  # Erste Zeile = Empfänger
