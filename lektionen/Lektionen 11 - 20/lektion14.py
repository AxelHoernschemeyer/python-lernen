# Lektion 14 - Eigenen Funktionen erstellen. (def = define)
#
# Aufgabe 1: Erstelle eine Funktion berechne_quadratzahl(zahl), die eine Zeile als Parameter
# entgegennimmt und deren Quadreatzahl (zahl * zahl) mit return zurückgibt.

def berechne_quadratzahl(zahl):
    """Test"""                      # <- Dokumentation für die Funktion.
    ergebnis = zahl * zahl
    return ergebnis

print(berechne_quadratzahl(5))
