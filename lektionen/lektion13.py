# Lektion 13 (Verschachtelte Schleifen)

# Aufgabe: Schreibe zwei ineinander verschachtelte for-Schleifen, die jeden 
# Vornamen mit jedem Nachnamen kombinieren und als vollständigen Namen ausgibt.
# (z.B. Axel Müller).

vorname = ["Axel", "Lena"]
nachname = ["Müller", "Weber"]
for name in vorname:
    for name2 in nachname:
        print(name, name2)  # <- An dieser Stelle ist es wichtig, auf die Einrückung zu achten. Ohne korrekte
                            #    korrekte Einrückung erfolgt eine Fehlermeldung.
