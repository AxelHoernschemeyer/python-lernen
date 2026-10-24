# Lektion 16 - Funktionen mit mehreren Rückgabewerten.
#
# Aufgabe 1:    Schreibe eine Funktion berechne_statistik(zahlen_liste), die eine Liste von Zahlen entgegennimmt.
#               Die Funktion soll drei Werte berechnen und mit return zurückgeben:
#                   Die Summe aller Zahlen
#                   Die Anzahl aller Zahlen
#                   Den gerundeten Durchschnitt (2 Stellen)
#               Rufe die Funktion mit der Liste 10, 20, 30, 40 auf, entpacke die drei Ergebnisse
#               beim Aufruf in drei Variablen gesamtsumme, anzahl, schnitt und gib sie mit print aus.

def berechne_statistik(zahlen_liste):
    """ Die Funktion ermittelt die Summe, die Anzahl und den Durchschnitt der Zahlen. """
    gesamtsumme = sum(zahlen_liste)
    anzahl      = len(zahlen_liste)
    schnitt     = round(sum(zahlen_liste) / (len(zahlen_liste)),2)    # <- Geht so. Die Berechnung wird hier jedoch doppelt ausgeführt.
    #schnitt     = round(gesamtsumme / anzahl,2)                      # <- Besser, je nach Datenmenge ist die Berechnung schneller.
    return gesamtsumme, anzahl, schnitt
gesamtsumme, anzahl, schnitt = berechne_statistik([10,20,30,40])
print("Gesamtsumme: ", gesamtsumme)
print("Anzahl: ", anzahl)
print("Durchschnitt: ", schnitt)