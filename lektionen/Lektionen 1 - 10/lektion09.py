# Die For Schleife:

# for zahl in range(Startwert, Endwert, Schrittweite):
# Innerhalb der Schleife kann man dann mit der Variable "zahl" arbeiten.
# Rechnen ist ebenfalls möglich.
# Z.B.: (zahl + 1) * 2
# Oder range(0,11,2) -> 0, 2, 4, 6, 8, 10 <- Der dritte Wert gibt die Schrittweite an.
# Oder negativ rangen(10, 0, -1) -> 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 <- Der dritte Wert gibt die Schrittweite an.

# Beispiele:
# 11 wird nicht ausgegeben
for Zahl in range(0,11):
    print(Zahl) 

# 10 wird 0 wird nicht ausgegeben. Rückwärts zählen mit -1 als Schrittweite.
for Zahl in range(10,0,-1):
    print(Zahl)

# 0, 2, 4, 6, 8, 10 <- Der dritte Wert gibt die Schrittweite an.
for zahl in range(0, 11,2):
    print(zahl)