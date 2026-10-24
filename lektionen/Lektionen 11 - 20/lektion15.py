# Lektion 15 - Mehrere Parameter an eine Funktion übergeben und Rückgabewerte erstellen.
#
# Aufgabe 1: Schreibe eine Funktion berechne_preis(netto, mwst_satz=19) 
#            für den Bruttopreis (brutto = netto * (1 + mwst_satz / 100)).
#            Gib das Ergebnis mit return gerundet (!) auf zwei Nachkommastellen zurück
#            Teste mit print(berechne_preis(100)) (nutzt 19%) und 
#            print(berechne_preis(100,7)) (nutzt 7%).

def berechne_preis(netto, mwst_satz=19):
    """ Preisberechnung unter Berücksichtiung eines Steuersatzes. """
    brutto = netto * (1 + mwst_satz / 100)
    return round(brutto,2)

print(berechne_preis(100))
print(berechne_preis(100,7))

