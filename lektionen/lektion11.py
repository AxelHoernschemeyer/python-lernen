# Durch Listen interieren
# Die for Schleife.
#   Die for-Schleife durchläuft automatisch alle Elemente einer Liste.

# zahlen = [10, 20, 30, 40]
# summe = 0

# for zahl in zahlen:
#     summe += zahl

# print(summe)

# zahlen = [10, 45, 23, 99, 12]
# max_zahl = 0

# for zahl in zahlen:
#     if max_zahl < zahl:
#         max_zahl = zahl
# print(max_zahl)

#  zahlen = [10, 45, 23, 99, 12]
#  min_zahl = 0

# for zahl in zahlen:
#     if min_zahl > zahl or min_zahl == 0:
#         min_zahl = zahl
# print(min_zahl)

zahlen = [12, 5, 8, 21, 3, 14]

# Startwert ist das erste Element der Liste
min_zahl = zahlen[0]

for zahl in zahlen:
    if zahl < min_zahl:
        min_zahl = zahl
print(min_zahl)  # Ergebnis: 3