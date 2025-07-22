import csv # Importiert das Modul zum Lesen und Schreiben von CSV-Dateien
import datetime

x=datetime.datetime.now()

artikel_liste = [] #Liste mit allen Artikeln
kunden_liste = [] # Liste mit allen Kunden
warenkorb = [] # Temporärer Warenkorb
bestellungen = []
#Rabatte
rabatt_aktiv = False
rabatt_prozent = 10
min_bestellwert = 50.0

class Kunde:
    def __init__(self,id,name,benutzername,passwort,strasse, plz, ort):
        self.id = id
        self.name = name
        self.benutzername = benutzername
        self.passwort = passwort
        self.strasse = strasse
        self.plz = plz
        self.ort = ort

def kunden_speichern(dateiname="kunden.csv"):
    with open(dateiname,mode="w", encoding="utf-8",newline="") as k_liste:
        writer=csv.writer(k_liste)
        writer.writerow(["ID", "Name","Benutzername", "Passwort", "Strasse","PLZ", "Ort"])
        for kunde in kunden_liste:
            writer.writerow([kunde.id, kunde.name,kunde.benutzername, kunde.passwort, kunde.strasse, kunde.plz, kunde.ort])

def kunden_laden(dateiname="kunden.csv"):
    global kunden_liste
    kunden_liste.clear()
    try:
        with open(dateiname,mode= "r", encoding="utf-8",newline="") as k_liste:
            reader= csv.reader(k_liste)
            next(reader)             #Die erste Zeile wird übersprungen da dort keine echten kundendaten stehen.
            for row in reader:
                if len(row) == 7 and all(row):
                 id,name,benutzername,passwort,strasse,plz,ort = row
                 kunden_liste.append(Kunde(int(id),name,benutzername,passwort,strasse,plz,ort))
    except FileNotFoundError:
        pass

def artikel_suchen():
    suchbegriff = input("Wir haben eine große Auswahl an Artikel, was suchen sie genau ? ").strip().lower()
    gefundene_artikel = []

    for artikel in artikel_liste:
        if suchbegriff in artikel.titel.lower() or suchbegriff in artikel.beschreibung.lower() or suchbegriff in artikel.kategorie.lower():
            gefundene_artikel.append(artikel)

    if not gefundene_artikel:
        print("Keine Artikel gefunden.")
    else:
        print("\nGefundene Artikel:")
        for artikel in gefundene_artikel:
            print(f"""
ID: {artikel.id}
Titel: {artikel.titel}
Größe: {artikel.groesse}
Beschreibung: {artikel.beschreibung}
Preis: {artikel.preis} €
Bestand: {artikel.bestand}
Kategorie: {artikel.kategorie}
-----------------------------""")

def artikel_nach_preis_anzeigen():
    print("\nVerfügbare Kategorien:")
    print("1. Preisspanne 0 bis 15")
    print("2. Preisspanne 15 bis 30")
    print("3. Preisspanne 30 bis 45")

    auswahl = input("Welche Preisspanne möchten sie sehen : ").strip()

    if auswahl == "1":
        min_preis = 0
        max_preis = 15
    elif auswahl == "2":
        min_preis = 15
        max_preis= 30
    elif auswahl == "3":
        min_preis = 30
        max_preis = 45
    else:
        print("Ungültige Auswahl.")
        return

    gefundene_artikel = [artikel for artikel in artikel_liste if min_preis <= artikel.preis <= max_preis]

    if not gefundene_artikel:
        print(f"Keine Artikel in der Preisspanne {min_preis} - {max_preis} gefunden.")
        return

    print(f"\n Artikel in der Preisspanne: {min_preis} - {max_preis} gefunden")
    for artikel in gefundene_artikel:
        print(f"""
ID: {artikel.id}
Titel: {artikel.titel}
Größe: {artikel.groesse}
Beschreibung: {artikel.beschreibung}
Preis: {artikel.preis} €
Bestand: {artikel.bestand}
Kategorie: {artikel.kategorie}
Erstellungsdatum: {artikel.erstellungsdatum}
-----------------------------""")

def artikel_nach_kategorie_anzeigen():
    print("\nVerfügbare Kategorien:")
    print("1. Textilien")
    print("2. Accessoires")
    print("3. Schreibwaren")

    auswahl = input("Welche Kategorie möchtest du anzeigen? (1–3): ").strip()

    if auswahl == "1":
        gewählte_kategorie = "Textilien"
    elif auswahl == "2":
        gewählte_kategorie = "Accessoires"
    elif auswahl == "3":
        gewählte_kategorie = "Schreibwaren"
    else:
        print("Ungültige Auswahl.")
        return

    gefundene_artikel = [artikel for artikel in artikel_liste if artikel.kategorie.lower() == gewählte_kategorie.lower()]

    if not gefundene_artikel:
        print(f"Keine Artikel in der Kategorie '{gewählte_kategorie}' gefunden.")
        return

    print(f"\n Artikel in der Kategorie: {gewählte_kategorie}")
    for artikel in gefundene_artikel:
        print(f"""
ID: {artikel.id}
Titel: {artikel.titel}
Größe: {artikel.groesse}
Beschreibung: {artikel.beschreibung}
Preis: {artikel.preis} €
Bestand: {artikel.bestand}
Kategorie: {artikel.kategorie}
Erstellungsdatum: {artikel.erstellungsdatum}
-----------------------------""")

class Artikel:
    def __init__(self,id,erstellungsdatum,titel,groesse,beschreibung,preis,bestand,kategorie):
        self.id = id
        self.erstellungsdatum = erstellungsdatum
        self.titel = titel
        self.groesse = groesse
        self.beschreibung = beschreibung
        self.preis = preis
        self.bestand = bestand
        self.kategorie = kategorie

def artikel_speichern(dateiname="artikel.csv"):
    with open(dateiname,mode="w",encoding="utf-8",newline="") as a_liste:
        writer = csv.writer(a_liste)
        writer.writerow(["ID","Erstellungsdatum", "Titel","Grösse", "Beschreibung", "Preis", "Bestand", "Kategorie"])
        for artikel in artikel_liste:
            writer.writerow([artikel.id,artikel.erstellungsdatum,artikel.titel,artikel.groesse, artikel.beschreibung, artikel.preis, artikel.bestand, artikel.kategorie])

def artikel_laden(dateiname="artikel.csv"):
    try:
        with open(dateiname,mode="r",encoding="utf-8") as a_liste:
            reader = csv.reader(a_liste)
            next(reader)
            for row in reader:
                if len(row) == 8:
                    id,erstellungsdatum,titel,groesse,beschreibung,preis,bestand,kategorie = row
                    artikel_liste.append(Artikel(id,erstellungsdatum,titel,groesse,beschreibung,float(preis),int(bestand),kategorie))
    except FileNotFoundError:
        pass

def artikel_hinzufuegen():
    print("\n--- Artikel hinzufügen ---")
    id = input("Artikel-ID: ")
    erstellungsdatum = x.strftime("%d/%m/%Y") #Formatierung der import datime damit es besser aussieht
    titel = input("Titel: ")
    groesse = input("Groesse: ")
    beschreibung = input("Beschreibung: ")
    preis = float(input("Preis: "))
    bestand = int(input("Lagerbestand: "))
    print("Kategorien: Textilien, Accessoires, Schreibwaren")
    kategorie = input("Kategorie: ")

    artikel = Artikel(id,erstellungsdatum,titel,groesse, beschreibung, preis, bestand, kategorie)
    artikel_liste.append(artikel)
    artikel_speichern()
    print(f"Artikel '{titel}' wurde hinzugefügt und gespeichert.")

def artikel_loeschen():
    artikel_id = input("Gib die ID des zu löschenden Artikels ein: ")

    for artikel in artikel_liste:
        if artikel.id == artikel_id:
            artikel_liste.remove(artikel)
            artikel_speichern()
            print(f"Artikel '{artikel.titel}' wurde gelöscht.")
            return
    print("Artikel mit dieser ID wurde nicht gefunden.")

def artikel_bearbeiten():
    artikel_id= input("Gib die ID des zu bearbeitenden Artikels ein: ")
    for artikel in artikel_liste:
        if artikel.id == artikel_id:
            print(f"Artikel {artikel.titel} gefunden. \nName: {artikel.titel} \nBeschreibung: {artikel.beschreibung} \nGröße: {artikel.groesse} \nPreis: {artikel.preis} \nBestand: {artikel.bestand} \nKategorie: {artikel.kategorie}\n")

            neuer_titel = input(f"Neuer Titel (aktuell: {artikel.titel}): ").strip()
            if neuer_titel:
                artikel.titel = neuer_titel

            neue_beschreibung = input(f"Neue Beschreibung (aktuell: {artikel.beschreibung}): ").strip()
            if neue_beschreibung:
                artikel.beschreibung = neue_beschreibung

            neue_groesse = input(f"Neue Größe (aktuell: {artikel.groesse}): ").strip()
            if neue_groesse:
                artikel.groesse = neue_groesse

            eingabe = input(f"Neuer Preis (aktuell: {artikel.preis}): ").strip()
            if eingabe:
                artikel.preis = float(eingabe)

            eingabe = input(f"Neuer Bestand (aktuell: {artikel.bestand}): ")
            if eingabe:
                artikel.bestand = float(eingabe)

            neue_kategorie = input(f"Neue Kategorie (aktuell: {artikel.kategorie}): ")
            if neue_kategorie:
                artikel.kategorie = neue_kategorie

            artikel_speichern()

            print("Artikel wurde erfolgreich bearbeitet")

            return

        else:
            print(f"Artikel mit {artikel_id} wurde nicht gefunden.")
            return

def artikel_rabatt():
    global rabatt_aktiv
    print("\n--- Rabatt-Einstellungen ---")
    if rabatt_aktiv:
        print("Ein Rabatt ist derzeit aktiv")
        wahl=input("Möchtest du den Rabatt deaktivieren? j/n ").strip()
        if wahl== "j":
            rabatt_aktiv = False
        else:
            print("Rabatt bleibt aktiv")

    else:
        print("Derzeit ist kein Rabatt aktiv")
        wahl=input("Möchtest du den rabatt aktivieren? j/n ").strip()
        if wahl== "j":
            rabatt_aktiv= True
            print(f"Der Rabatt von {rabatt_prozent}% ab einem Mindestbestellwert von {min_bestellwert:.2f} € wurde aktiviert.")
        else:
            print("Rabatt bleibt deaktiviert")

def artikel_in_warenkorb():
    print("\n Artikel in den Warenkorb legen ")
    artikel_id = input("Gib die Artikel-ID ein, die du hinzufügen möchtest: ").strip() # strip enfernt leerzeichen
    gefunden = False  # Noch kein Artikel gefunden wir gehen davon aus das der Artikel nicht exestiert
    # Wir suchen jetzt da der ID
    for artikel in artikel_liste:
        if artikel.id == artikel_id:
            print(f"Gefunden: {artikel.titel} – {artikel.preis:.2f} € – Grösse: {artikel.groesse} Lager: {artikel.bestand}") #.2f macht aus 12.5 = 12.50
            menge = input("Wie viele möchtest du hinzufügen? ")
            if menge.isdigit():  # Prüfe, ob Eingabe eine gültige Zahl ist
                menge = int(menge)
                if menge > 0 and menge <= artikel.bestand:
                    warenkorb.append((artikel, menge))
                    print(f"{menge}x {artikel.titel} in Größe {artikel.groesse} zum Warenkorb hinzugefügt.")
                else:
                    print("Ungültige Menge – entweder zu viel oder nicht vorhanden.")
            else:
                print("Bitte eine gültige Zahl eingeben.")
            gefunden = True
            break  # Schleife beenden, da Artikel-ID eindeutig ist

    if not gefunden:
        print("Kein Artikel mit dieser ID gefunden.")

def warenkorb_anzeigen():
    print("\n--- Dein Warenkorb ---")
    if not warenkorb:
        print("Der Warenkorb ist leer.")
        return

    gesamtpreis = 0
    for artikel, menge in warenkorb:
        einzelpreis = artikel.preis
        zwischensumme = einzelpreis * menge
        gesamtpreis += zwischensumme
        print(f"{menge}x {artikel.titel} ({einzelpreis:.2f} € / Stk.) – Zwischensumme: {zwischensumme:.2f} €")

    print(f"\nGesamtpreis: {gesamtpreis:.2f} €")

    # Rabatt anzeigen, aber noch nicht abziehen (das macht warenkorb_bestellen)
    if rabatt_aktiv and gesamtpreis >= min_bestellwert:
        rabatt_betrag = gesamtpreis * (rabatt_prozent / 100)
        neuer_gesamtpreis = gesamtpreis - rabatt_betrag
        print(f"Rabatt aktiviert: -{rabatt_betrag:.2f} € ({rabatt_prozent}% Rabatt)")
        print(f"Endpreis nach Rabatt: {neuer_gesamtpreis:.2f} €")
    elif rabatt_aktiv:
        differenz = min_bestellwert - gesamtpreis
        print(f"(Rabatt aktiv, aber du musst noch {differenz:.2f} € mehr kaufen für den Rabatt von {rabatt_prozent}%)")

def warenkorb_bestellen(kundenname):
    print("\n--- Bestellung abschließen ---")

    if not warenkorb:
        print("Dein Warenkorb ist leer. Bestellung nicht möglich.")
        return

    gesamtpreis = 0
    for artikel, menge in warenkorb:
        zwischensumme = artikel.preis * menge
        gesamtpreis += zwischensumme

    rabatt_betrag = 0
    if rabatt_aktiv and gesamtpreis >= min_bestellwert:
        rabatt_betrag = gesamtpreis * (rabatt_prozent / 100)
        gesamtpreis -= rabatt_betrag
        print(f"Rabatt von {rabatt_prozent}% angewendet: -{rabatt_betrag:.2f} €")

    print(f"\nEndpreis deiner Bestellung: {gesamtpreis:.2f} €")

    for artikel, menge in warenkorb:
        artikel.bestand -= menge

        if artikel.bestand < 0:
            artikel.bestand = 0  # Sicherheit



    artikel_speichern()
    bestellung_speichern_csv(kundenname, warenkorb, gesamtpreis)
    warenkorb.clear()
    print("Deine Bestellung wurde erfolgreich abgeschlossen.")

def artikel_aus_warenkorb_entfernen():
    artikel_id = input("Welche Artikel-ID soll entfernt werden? ").strip()

    for i, (artikel, menge) in enumerate(warenkorb):
        if artikel.id == artikel_id:
            print(f"Im Warenkorb: {menge}x {artikel.titel}")
            anzahl = input("Wie viele möchtest du entfernen? ").strip()

            if anzahl.isdigit():
                anzahl = int(anzahl)

                if anzahl >= menge:
                    del warenkorb[i]
                    print("Artikel komplett entfernt.")
                elif anzahl > 0:
                    warenkorb[i] = (artikel, menge - anzahl)
                    print(f"{anzahl} Stück entfernt. Noch {menge - anzahl} im Warenkorb.")
                else:
                    print("Bitte gib eine Zahl größer als 0 ein.")
            else:
                print("Ungültige Eingabe.")
            return

    print("Artikel nicht im Warenkorb gefunden.")

def bericht_anzeigen():
    print("\n--- Bericht für die Geschäftsführung ---")
    dateiname = "bestellungen.csv"

    try:
        with open(dateiname, mode="r", encoding="utf-8") as datei:
            reader = csv.DictReader(datei)
            bestellungen = list(reader)

    except FileNotFoundError:
        print("Keine Bestellungen vorhanden.")
        return

    start_datum = input("Gib ein Startdatum ein (Format: TT.MM.JJJJ): ")
    end_datum = input("Gib ein Enddatum ein (Format: TT.MM.JJJJ): ")

    def zeitspanne(datum_str):
        try:
            return datetime.datetime.strptime(datum_str, "%d.%m.%Y")
        except:
            print("Falsches Datum.")
            return None

    start = zeitspanne(start_datum)
    end = zeitspanne(end_datum)

    if not start or not end:
        return

    # Filtere relevante Bestellungen nach Zeitraum
    gefilterte_bestellungen = []
    for b in bestellungen:
        zeitstempel = b["Datum"].split()[0]  # Datum ohne Uhrzeit
        zeit_objekt = zeitspanne(zeitstempel)
        if zeit_objekt and start <= zeit_objekt <= end:
            gefilterte_bestellungen.append(b)

    if not gefilterte_bestellungen:
        print("Keine Bestellungen im Zeitraum gefunden.")
        return

    # Anzahl der Bestellungen
    kunden_bestellungen = {}
    for b in gefilterte_bestellungen:
        kunde = b["Kunde"]
        gesamt = float(b["Gesamtpreis"])
        if kunde not in kunden_bestellungen:
            kunden_bestellungen[kunde] = []
        kunden_bestellungen[kunde].append(gesamt)

    anzahl_bestellungen = sum(len(v) for v in kunden_bestellungen.values())
    umsatz = sum(float(b["Gesamtpreis"]) for b in gefilterte_bestellungen)

    print(f"\nZeitraum: {start_datum} bis {end_datum}")
    print(f"Anzahl der Bestellungen: {anzahl_bestellungen}")
    print(f"Gesamtumsatz: {umsatz:.2f} €")

    # Umsatzanteile je Artikel berechnen
    artikel_umsatz = {}
    for b in gefilterte_bestellungen:
        titel = b["Artikel-Titel"]
        betrag = float(b["Zwischensumme"])
        artikel_umsatz[titel] = artikel_umsatz.get(titel, 0) + betrag

    print("\nUmsatz:")
    sortiert = sorted(artikel_umsatz.items(), key=lambda x: x[1], reverse=True)

    for titel, betrag in sortiert:
        anteil = (betrag / umsatz) * 100
        print(f"{titel}: {betrag:.2f} € ({anteil:.1f}%)")

def bestellung_speichern_csv(kundenname, bestellte_artikel, gesamtpreis):
    dateiname = "bestellungen.csv"
    kopfzeile = ["Datum", "Kunde", "Artikel-ID", "Artikel-Titel", "Menge", "Einzelpreis", "Zwischensumme", "Gesamtpreis"]

    # Versuche Datei zu öffnen – wenn das fehlschlägt, ist sie neu
    datei_neu = False
    try:
        with open(dateiname, mode="r", encoding="utf-8") as f:
            pass  # Datei existiert
    except FileNotFoundError:
        datei_neu = True  # Datei existiert noch nicht

    with open(dateiname, mode="a", encoding="utf-8", newline="") as datei:
        writer = csv.writer(datei)

        if datei_neu:
            writer.writerow(kopfzeile)

        datum = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

        for artikel, menge in bestellte_artikel:
            zwischensumme = artikel.preis * menge
            writer.writerow([datum, kundenname, artikel.id, artikel.titel, menge, artikel.preis, zwischensumme, gesamtpreis])

def kunden_anzeigen():
    print("\n Kundenliste")
    if not kunden_liste: # wenn die Liste leer wäre
       print("Es sind noch keine Kunden registriert")
       return # funktion beenden
    for kunde in kunden_liste:
        print(f"""
    ID: {kunde.id}
    Name: {kunde.name}
    Benutzername: {kunde.benutzername}
    Adresse: {kunde.strasse}, {kunde.plz} {kunde.ort}
    Passwort: {kunde.passwort}
     -----------------------------""")  # Trenner zur besseren Lesbarkeit

def verwaltungs_menue(): # Menüübersicht zur Ausführung der einzelenen Funktionen für die Verwaltung
    while True:
        print("\n--- Webshop Verwaltung ---")
        print("1. Artikel hinzufügen") # gemacht
        print("2. Artikel löschen")   #gemacht
        print("3. Artikel bearbeiten") #gemacht
        print("4. Rabatt Aktivieren") #gemacht
        print("5. Bericht Anzeigen")
        print("6. Kunden liste") #gemacht
        print("0. Abbrechen")
        auswahl = input()

        if auswahl == "1": artikel_hinzufuegen()  # gemacht
        elif auswahl == "2": artikel_loeschen()     #gemacht
        elif auswahl == "3": artikel_bearbeiten()  #gemacht
        elif auswahl == "4": artikel_rabatt()       #gemacht
        elif auswahl == "5": bericht_anzeigen()  #gemacht
        elif auswahl == "6": kunden_anzeigen()      #gemacht
        elif auswahl == "0": break
        else: print("Auswahl ungültig")

def kunden_menue(aktiver_kunde):
    while True:
        print("\n--- WI Fanshop ---")
        print("1. Artikel suchen") #gemacht
        print("2. Artikel anzeigen") #gemacht
        print("3. Artikel zum Warenkorb hinzufügen") #gemacht
        print("4. Warenkorb anzeigen") #gemacht
        print("5. Bestellung abschließen")
        print("6. Artikel aus Warenkorb entfernen")
        print("7. Artikel in einer Preisspanne anzeigen") # gemacht im test
        print("0. Abmelden")
        auswahl = input()

        if auswahl == "1": artikel_suchen() #gemacht
        elif auswahl == "2": artikel_nach_kategorie_anzeigen() #gemacht glaube ich mal LG TIm
        elif auswahl == "3": artikel_in_warenkorb() #gemacht
        elif auswahl == "4": warenkorb_anzeigen() #gemacht
        elif auswahl == "5": warenkorb_bestellen(aktiver_kunde.name) #gemacht
        elif auswahl == "6": artikel_aus_warenkorb_entfernen() #gemacht
        elif auswahl == "7": artikel_nach_preis_anzeigen()  # gemacht im test
        elif auswahl == "12345": verwaltungs_menue()
        elif auswahl == "0": return
        else: print("Auswahl ungültig")

def einleitung():
    kunden_laden() # Kundenliste muss erst geladen werden damit er überprüfen kann ob die Liste bereits vorhanden ist bz ob der Benutzername bereits in der Liste vorhanden ist
    print("Sind sie aktueller Kunde ?")
    member = input("1. Ja  / 2. Nein ")
    if member.isdigit(): #Überprüft ob der String eine Zahl ist und wenn ja, dann ist richtig
        member = int(member) #macht die Zahl von einem String zu einem Int()

        if member == 2:
            print("Bitte legen Sie ein Benutzerkonto an.")

            while True:
                benutzername = input ("Benutzername: ").strip()
                if any (k.benutzername == benutzername for k in kunden_liste): # Überprüft ob der in der Liste für den Kubdeb ob der Benutzername schon von einem anderen Kunden belegt wird
                    print("Benutzername ist schon vergeben. Wählen sie einen anderen.")
                else:
                    break # beendet die Schleife und geht dann im Code weiter

            name = input("Name: ")
            passwort = input("Passwort: ")
            strasse = input("Strasse: ")
            plz = input("PLZ: ")
            ort = input("Ort: ")

            neuer_kunde = Kunde(len(kunden_liste) + 1, name,benutzername, passwort, strasse, plz, ort) # Zählt die Liste durch und hängt an letzter stelle dann den neuen Kunden an
            kunden_liste.append(neuer_kunde)      #fügt den Kunden dann hinzu
            kunden_speichern() #speichert den Kunden dann in der Liste
            print (f"Konto für {name} wurde erstellt und gespeichert.")
            return neuer_kunde # neuer Kunde wird somit weiterverwendet

        elif member == 1: # wenn die eingabe halt 1 war dann :
            benutzername = input("Gebe deinen Benutzernamen ein:  ")
            passwort = input("Gebe dein Passwort ein: ")
            for kunde in kunden_liste: # überprüft ob der kunde in der Kundenliste ist
                if kunde.benutzername == benutzername and kunde.passwort == passwort: # schaut welcher Benutzernamen und Passwort übereinstimmen
                    print(f"Herzlichen Willkommen {kunde.name} ")
                    return kunde # Kunde der angemledet wurde wird somit weiterverwendet
            print("Benutzername oder Passwort sind falsch oder nicht gegeben.")
            return einleitung() # startet die Einleitung wieder

        else:
            print("Bitte bestätige mit 1 oder 2")
            return einleitung() # startet die Einleitung wieder

    else:
        print("Bitte gib nur eine Zahl ein, benutze keine Buchstaben")
        return einleitung() # startet die Einleitung wieder

def laden():
    kunden_laden()
    artikel_laden()

def hauptmenue():
    while True:
        aktiver_kunde = einleitung()
        kunden_menue(aktiver_kunde)

laden()
hauptmenue()
