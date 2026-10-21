# Lektion 10: Listen

# Listen werden in Python mit eckigen Klammern [] definiert. Sie können beliebige Datentypen enthalten, einschließlich anderer Listen.
# Eine Liste speichert mehrere Werte in einer einzigen Variablen.
# Beispiel: meine_liste = [1, 2, 3, "Hallo", [4, 5]]
# Ausgabe: print(meine_liste)  # Ausgabe: [1, 2, 3, 'Hallo', [4, 5]]
# Listen beginnen bei Index 0
# Erstes Element  = Liste[0]
# Zweites Element = Liste[1]
# Drittes Element = Liste[2]
# Wenn man einen Wert abfragen will, der nicht in der Liste aufgeführt ist, bekommt man einen Fehler.
#   IndexError: list index out of range
# List[index] = wert <- Ändert den Wert an der angegebenen Stelle.
# listenname.append("WERT") <- Wert wird am Ende angehängt
# print(len(staedte)) <- Liefert die Einträge der Liste
# === HINWEIS ====
# print[len(staedte) -1]
#   und 
# print(stadte[-1]) <- liefert den letzten Wert, -2 den vorletzen usw.
# Beide Ausgaben liefern den gleichen Wert.
# In der Praxis wird 'print(staedt[-1])' verwendet. Weniger Code und leichter zu lesen.

# Liste mit Städten
#staedte = ["Belm", "Osnabrück", "Bohmte", "Berlin", "Hamburg"]
#print(staedte[8])  # Ausgabe: Berlin

# Neue Liste mit Axel, Simone und Marie
#personen = ["Axel", "Simone", "Marie"]
#print(personen)

# List mit append erweitern
#staedte = ["Belm", "Osnabrück", "Berlin", "Hamburg"]
#staedte.append("Hamburg") # <- hängt einen Wert am Ende an.
#print(staedte)

#staedte = ["Belm", "Osnabrück", "Berlin", "Hamburg"]
#print(staedte[-2])


staedte = ["Belm", "Osnabrück", "Berlin", "Hamburg"]

print(len(staedte))
print(staedte[len(staedte) - 1])
print(staedte[-1])