# Lektion 17: Dateizugriffe (Dateien lesen & schreiben mit open()) 
#
# Konzept: Dateien in Python öffnen und verarbeiten 
# Um Dateien auf der Festplatte zu lesen oder zu beschneiden, nutzt man in Python die Funktion open().
# Der modernste und sicherste Weg ist der with-Block: Er sorgt dafür, dass die Datei automatisch wieder geschlossen und gespeichert
# wird, selbst wenn im Code ein Fehler auftritt. 
#
# Die drei wichtigsten Modi:
#   - "w" (write):      Erstellt eine neue Datei oder überschreibt eine bestehende Datei komplett.
#   - "a" (appende):    Hängt neuen Text an das Ende einer bestehenden Datei an.  
#   - "r" (read):       Liest Inhalt aus einer bestehenden Datei aus.
#
# Syntax Beispiele:
#   1.  In eine Datei schreiben ("w"):
#       with open("test.txt", "w", encoding="utf-8") as datei:
#           datei.write("Hallo Welt!\nDas ist die zweite Zeile.")
#   2.  Aus einer Datei lesen ("r"):
#       with open("test.txt", "r", encoding="utf-8") as datei:
#           inhalt = datei.read()
#           print(inhalt)
#   Hinweis: encoding="utf-8" stellt sicher, das Sonderzeichen und Umlaute
#       (ä, ö, ü, ß) sauber gelesen und geschrieben werden.
#
# Aufgabe:  Schreibe mit dem w-Modus den Text "Erste Zeile im Logfile\nZweite Zeile im Logfile" in eine Datei 
#           Namens "log.txt"
#           Öffne dieselbe Datei direkt danach im r-Modus, ließ den Inhalt mit .read() aus und gib ihn mit
#           print() in der Konsole aus.

with open("log.txt", "w", encoding="utf-8") as datei:
    datei.write("Erste Zeile im Logfile\nZwieite Zeile im Logfile")

with open("log.txt", "r", encoding="utf-8") as datei:
    inhalt = datei.read()
    print(inhalt)