# Lektion 12: Nützliche Funktionen für Listen
#
# Die wichtigsten eingebauten Funktionen:
#   len(liste):                 Gibt die Anzahl der Elemente in der Liste zurück.
#   sum(liste):                 Berechnet die Gesamtsumme aller Zahlen in der Liste.
#   min(liste) / max(liste):    Liefert den kleinsten bzw. größten Wert der Liste.
#
# Beispiele

namen = ["Axel", "Marie", "Simone", "Frank"]
print("len/Anzahl:", len(namen))    # <- Liefert in diesem Beispile 4 da 4 Einträge in der Liste stehen.

zahl = [2,2,1]
print("Sum: ", sum(zahl))           # <- Liefert die Summe der Zahlen aus der Liste. Hier 2+2+1 = 5.

zahl1 = [2,4,6,8]
print("Min: ", min(zahl1))          # <- Liefert die kleinest Zahl aus der Liste. Hier 2.

zahl2 = [1,3,5,7]
print("Max: ", max(zahl2))          # <- Liefert die größet Zahl aus der Liste. Hier 7.

zahl3 = [2,4,6]
print("Summe / Anzahl Einträge:", sum(zahl3)/len(zahl3))    # <- Mit diesen Funktionen kann gerechnet werden. Ergebnis hier
                                                            # 2+4+6 = 12 / 3 = 4.0