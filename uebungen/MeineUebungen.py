# In dieser Datei gibt es nur meine eigenen Übungen.

# Aufgabe 1: Benutzer nach Name und Alter fragen und eine Nachricht ausgeben

    # name = input("Wie heißt du? ")
    # alter = int(input("Wie alt bist du? "))

    # if alter < 13:
    #     print(f"Hallo {name}, du bist ein Kind.")
    # elif 13 <= alter < 18:
    #     print(f"Hallo {name}, du bist ein Teenager.")   
    # else:
    #     print(f"Hallo {name}, du bist {alter} und du bist erwachsen.")

# Aufgabe 2: Benutzer nach einer Zahl fragen und prüfen, ob sie gerade oder ungerade ist

    # zahl1 = int(input("Bitte geben Sie die erste Zahl ein: "))
    # if zahl1 % 2 == 0:
    #     print(f"Die Zahl {zahl1} ist gerade.")
    # else:
    #     print(f"Die Zahl {zahl1} ist ungerade.")    

# Aufgabe 3: Schreibe ein Programm, das sich eine Zahl zwischen 1 und 100 ausdenkt.
# Der Benutzer muss raten, welche Zahl es ist. Am Ende soll das Programm ausgeben, wie viele
# Versuche der Benutzer gebraucht hat, um die Zahl zu erraten.

import random

zufallszahl = random.randint(1, 100)
versuche = 0
geraten = False

print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Versuche sie zu erraten!")

while not geraten:
    benutzerzahl = int(input("Gib deine Vermutung ein: "))
    versuche += 1

    if benutzerzahl < zufallszahl:
        print("Zu niedrig! Versuch es noch einmal.")
    elif benutzerzahl > zufallszahl:
        print("Zu hoch! Versuch es noch einmal.")
    else:
        geraten = True
        print(f"Herzlichen Glückwunsch! Du hast die Zahl {zufallszahl} in {versuche} Versuchen erraten.")
