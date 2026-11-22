""" Datenbankanbindung aufbauen und abfragen ausführen. """
#   =========================================
#   Erstellt von Axel Hörnschemeyer
#   Stand: 1.00
#   eMail: axel.hoernschemeyer@googlemail.com
#   =========================================

import config
import oracledb

def get_all_vendor(pwd):
    """ Namen der Kreditoren auslesen und zurückgeben. """
    db_password = pwd
    verbindung = oracledb.connect(
        user=config.DB_USER,
        password=db_password,
        dsn=config.DSN
        )
    cursor = verbindung.cursor()
    # Abfrage
    cursor.execute("SELECT NAME FROM KREDITOREN")
    daten = cursor.fetchall()
    laenge = len(daten)
    vendor = []
    for zeile in range(laenge):
        vendor.append(daten[zeile][0])
    cursor.close()
    verbindung.close()
    return vendor

def get_vendor_id(vendor_name, pwd):
    """ ID des Kreditoren auslesen und zurückgeben. """
    db_password = pwd
    verbindung = oracledb.connect(
        user=config.DB_USER,
        password=db_password,
        dsn=config.DSN
        )
    cursor = verbindung.cursor()
    # Abfrage der Kreditoren-ID basierend auf dem Namen
    cursor.execute("SELECT ID FROM KREDITOREN WHERE NAME = :1", (vendor_name,))
    daten = cursor.fetchone()
    vendor_id = daten[0] if daten else None
    cursor.close()
    verbindung.close()
    return vendor_id

def get_tarif_id(tarif_name, pwd):
    """ ID des Tarifs auslesen und zurückgeben. """
    db_password = pwd
    verbindung = oracledb.connect(
        user=config.DB_USER,
        password=db_password,
        dsn=config.DSN
        )
    cursor = verbindung.cursor()
    # Abfrage der Tarif-ID basierend auf dem Namen
    cursor.execute("SELECT ID FROM TARIFE WHERE BEZEICHNUNG = :1", (tarif_name,))
    daten = cursor.fetchone()
    tarif_id = daten[0] if daten else None
    cursor.close()
    verbindung.close()
    return tarif_id

def rechnung_existiert(rg_nummer, kreditor_id, pwd):
    """Prüft ob die Rechnung mit Rechnungsnummer und Kreditor-ID schon existiert."""
    sql = "SELECT COUNT(*) FROM RECHNUNGS_KOPF WHERE RG_NUMMER = :1 AND KREDITOR_ID = :2"

    con = oracledb.connect(user=config.DB_USER, password=pwd, dsn=config.DSN)
    cursor = con.cursor()
    cursor.execute(sql, (rg_nummer,kreditor_id))

    # fetchone() [0] holt die reine Trefferanzahl (0 oder +1)
    anzahl = cursor.fetchone() [0]

    cursor.close
    con.close

    return anzahl > 0

def speichere_rechnung(kreditor_id, tarif_id, file_name, details, pwd):
    """ Rechnung in der Datenbank speichern."""
    db_password = pwd

    try:
        verbindung = oracledb.connect(
            user=config.DB_USER,
            password=db_password,
            dsn=config.DSN
            )
        cursor = verbindung.cursor()
        # Betrag und Steuer in Zahlen umwandeln (Komma durch Punkt ersetzen)
        ust_satz = float(details.get("USt-Satz", "0").replace(",", "."))
        zeitraum_str = details.get("Zeitraum", "")  # z. B. "01.09.-30.09.2026"

        von_datum = None
        bis_datum = None

        if "-" in zeitraum_str:
            von_teil, bis_datum = zeitraum_str.split("-")
            von_teil = von_teil.strip()   # "01.09."
            bis_datum = bis_datum.strip() # "30.09.2026"

            # Jahr aus dem Enddatum ("30.09.2026") herausholen ("2026")
            jahr = bis_datum.split(".")[-1]

            # Falls beim Startdatum das Jahr fehlt (z. B. "01.09."), fügen wir das Jahr an:
            if von_teil.endswith("."):
                von_datum = f"{von_teil}{jahr}"       # "01.09.2026"
            else:
                von_datum = f"{von_teil}.{jahr}"

        # Datenreihenfolge, wie sie in den Details stehen:
        #   0: Kunden-Nr.,
        #   1: Rechnungsdatum,
        #   2: Rufnummer,
        #   3: Tarif,
        #   4: Rechnungsnummer,
        #   5: USt-Satz,
        #   6: Rechnungsbetrag
        #   7: Zeitraum
        #   8: Nettorechnungsbetrag
        #   9: Bruttobetrag
        #   10: Ust-Betrag
        sql = """
            INSERT INTO RECHNUNGS_KOPF (KREDITOR_ID, KUNDEN_NUMMER, RG_DATUM, RUFNUMMER, TARIF_ID, RG_NUMMER, UST_SATZ, RG_ZEITRAUM_VON, RG_ZEITRAUM_BIS, DATEINAME_IMP, BETRAG_NETTO,BETRAG_BRUTTO,UST_BETRAG,KUNDENNAME)
            VALUES (:1, :2, TO_DATE(:3, 'DD.MM.YYYY'), :4, :5, :6, :7, TO_DATE(:8, 'DD.MM.YYYY'), TO_DATE(:9, 'DD.MM.YYYY'), :10, :11, :12, :13, :14)
        """
        cursor.execute(sql, (
            kreditor_id,
            details.get("Kunden-Nr.", ""),
            details.get("Rechnungsdatum", ""),
            details.get("Rufnummer", ""),
            tarif_id,
            details.get("Rechnungsnummer", ""),
            ust_satz,
            von_datum,
            bis_datum,
            file_name,
            details.get("NettoRGbetrag", ""),
            details.get("Rechnungsbetrag", ""),
            details.get("USt-Betrag", ""),
            details.get("Empfänger", "")
        ))
        verbindung.commit()
        cursor.close()
        verbindung.close()
        print("✅ Rechnung erfolgreich in Oracle gespeichert!")

    except oracledb.InterfaceError as e:
        print(f"❌ Datenbankfehler: {e}")
