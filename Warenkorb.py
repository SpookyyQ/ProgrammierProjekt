import csv       # Importiert das Modul zum Lesen und Schreiben von CSV-Dateien
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
    with open(dateiname,mode="w", encoding="utf-8") as k_liste:
        writer=csv.writer(k_liste)
        writer.writerow(["ID", "Name","Benutzername", "Passwort", "Strasse","PLZ", "Ort"])
        for kunde in kunden_liste:
            writer.writerow([kunde.id, kunde.name,kunde.benutzername, kunde.passwort, kunde.strasse, kunde.plz, kunde.ort])

def kunden_laden(dateiname="kunden.csv"):
    try:
        with open(dateiname,mode= "r", encoding="utf-8") as k_liste:
            reader= csv.reader(k_liste)
            next(reader)             #Die erste Zeile wird übersprungen da dort keine echten kundendaten stehen.
            for row in reader:
                if len(row) == 7:
                 id,name,benutzername,passwort,strasse,plz,ort = row
                 kunden_liste.append(Kunde(int(id),name,benutzername,passwort,strasse,plz,ort))
    except FileNotFoundError:
        pass

def artikel_suchen():
    suchbegriff = input("Wir haben eine große Auswahl an Artikel, was suchen sie genau ?").strip()
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
Beschreibung: {artikel.beschreibung}
Preis: {artikel.preis} €
Bestand: {artikel.bestand}
Kategorie: {artikel.kategorie}
-----------------------------""")

#def zum laden der Menüpunkte
def artikel_kategorien():
    while True:
        print("\n--- Kategorien ---")
        print("1. Textilien")
        print("2. Accessoires")
        print("3. Schreibwaren")
        print("0. Zurück")
        auswahl = input()
        if auswahl == "1": Textilien()
        elif auswahl == "2": Accessoires()
        elif auswahl == "3": Schreibwaren()
        elif auswahl == "0": kunden_menue()
        else: print("auswahl ungültig")

class Artikel:
    def __init__(self,id,titel,beschreibung,preis,bestand,kategorie):
        self.id = id
        self.titel = titel
        self.beschreibung = beschreibung
        self.preis = preis
        self.bestand = bestand
        self.kategorie = kategorie
#artikel in csv speichern
def artikel_speichern(dateiname="artikel.csv"):
    with open(dateiname,mode="w",encoding="utf-8",newline="") as a_liste:
        writer = csv.writer(a_liste)
        writer.writerow(["ID", "Titel", "Beschreibung", "Preis", "Bestand", "Kategorie"])
        for artikel in artikel_liste:
            writer.writerow([artikel.id, artikel.titel, artikel.beschreibung, artikel.preis, artikel.bestand, artikel.kategorie])

#Artikel aus CSV laden
def artikel_laden(dateiname="artikel.csv"):
    try:
        with open(dateiname,mode="r",encoding="utf-8") as a_liste:
            reader = csv.reader(a_liste)
            next(reader)
            for row in reader:
                if len(row) == 6:
                    id,titel,beschreibung,preis,bestand,kategorie = row
                    artikel_liste.append(Artikel(id,titel,beschreibung,float(preis),int(bestand),kategorie))
    except FileNotFoundError:
        pass

def artikel_hinzufuegen():
    print("\n--- Artikel hinzufügen ---")
    id = input("Artikel-ID: ")
    titel = input("Titel: ")
    beschreibung = input("Beschreibung: ")
    preis = float(input("Preis: "))
    bestand = int(input("Lagerbestand: "))
    print("Kategorien: Textilien, Accessoires, Schreibwaren")
    kategorie = input("Kategorie: ")

    artikel = Artikel(id, titel, beschreibung, preis, bestand, kategorie)
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
            print(f"Artikel {artikel.titel} gefunden. \nName: {artikel.titel} \nBeschreibung: {artikel.beschreibung} \nPreis: {artikel.preis} \nBestand: {artikel.bestand} \nKategorie: {artikel.kategorie}\n")

            neuer_titel = input(f"Neuer Titel (aktuell: {artikel.titel}): ").strip()
            if neuer_titel:
                artikel.titel = neuer_titel

            neue_beschreibung = input(f"Neue Beschreibung (aktuell: {artikel.beschreibung}): ").strip()
            if neue_beschreibung:
                artikel.beschreibung = neue_beschreibung

            neuer_preis = float(input(f"Neuer Preis (aktuell: {artikel.preis}): "))
            if neuer_preis:
                artikel.preis = neuer_preis

            neuer_bestand = int(input(f"Neuer Bestand (aktuell: {artikel.bestand}): "))
            if neuer_bestand:
                artikel.bestand = neuer_bestand

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

##########Kundenlsite#######
#Funktion zum Hinzufügen eines Artikels in den Warenkorb#
def artikel_in_warenkorb():
    print("\n Artikel in den Warenkorb legen ")
    artikel_id = input("Gib die Artikel-ID ein, die du kaufen möchtest: ").strip() # strip enfernt leerzeichen
    gefunden = False  # Noch kein Artikel gefunden wir gehen davon aus das der Artikel nicht exestiert
    # Wir suchen jetzt da der ID
    for artikel in artikel_liste:
        if artikel.id == artikel_id:
            print(f"Gefunden: {artikel.titel} – {artikel.preis:.2f} € – Lager: {artikel.bestand}") #.2f macht aus 12.5 = 12.50
            menge = input("Wie viele möchtest du kaufen? ")
            if menge.isdigit():  # Prüfe, ob Eingabe eine gültige Zahl ist
                menge = int(menge)
                if menge > 0 and menge <= artikel.bestand:
                    # Artikel und Menge als Tupel in Warenkorb legen
                    warenkorb.append((artikel, menge))
                    print(f"{menge}x '{artikel.titel}' zum Warenkorb hinzugefügt.")
                else:
                    print("Ungültige Menge – entweder zu viel oder nicht vorhanden.")
            else:
                print("Bitte eine gültige Zahl eingeben.")
            gefunden = True
            break  # Schleife beenden, da Artikel-ID eindeutig ist

        if not gefunden:
            print("Kein Artikel mit dieser ID gefunden.")


    while True:
        weiterer_artikel = input("Wollen sie einen weiteren Artikel kaufen ? j/n ").strip().lower()
        if weiterer_artikel == "j":
            artikel_in_warenkorb()
            break

        elif weiterer_artikel == "n":
            kunden_menue()
            break

        else:
            print("Bitte bestätigen sie mit j oder n ")


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

########Kundenliste#####
def verwaltungs_menue():
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
        elif auswahl == "5": bericht_anzeigen()
        elif auswahl == "6": kunden_anzeigen()      #gemacht
        elif auswahl == "0": break
        else: print("Auswahl ungültig")

def kunden_menue():
    while True:
        print("\n--- WI Fanshop ---")
        print("1. Artikel suchen") #gemacht
        print("2. Artikel anzeigen")  # gemacht
        print("3. Artikel in Warenkorb") #gemacht
        print("4. Warenkorb anzeigen")
        print("5. Bestellung abschließen")
        print("0. Abmelden")
        auswahl = input()

        if auswahl == "1": artikel_suchen() #gemacht
        elif auswahl == "2": artikel_kategorien() # gemacht
        elif auswahl == "3": artikel_in_warenkorb() #gemacht
        elif auswahl == "4": warenkorb_anzeigen()
        elif auswahl == "5": warenkorb_bestellen()
        elif auswahl == "12345": verwaltungs_menue()
        elif auswahl == "0": einleitung()
        else: print("Auswahl ungültig")

def einleitung():
    kunden_laden()
    print("Sind sie aktueller Kunde ?")
    member = input("1. Ja  / 2. Nein ")
    if member.isdigit(): #Überprüft ob der String eine Zahl ist und wenn ja, dann ist richtig
        member = int(member) #macht die Zahl von einem String zu einem Int()

        if member == 2:
            print("Bitte legen Sie ein Benutzerkonto an.")

            while True:
                benutzername = input ("Benutzername: ").strip()
                if any (k.benutzername == benutzername for k in kunden_liste):
                    print("Benutzername ist schon vergeben. Wählen sie einen anderen.")
                else:
                    break

            name = input("Name: ")
            passwort = input("Passwort: ")
            strasse = input("Strasse: ")
            plz = input("PLZ: ")
            ort = input("Ort: ")

            neuer_kunde = Kunde(len(kunden_liste) + 1, name,benutzername, passwort, strasse, plz, ort)
            kunden_liste.append(neuer_kunde)      #einmal nachlesen angeblich wird hier ein Kundenobjekt gemacht und in Kunden_liste abgespeichert
            kunden_speichern()
            print (f"Konto für {name} wurde erstellt und gespeichert.")
            return neuer_kunde

        elif member == 1:
            benutzername = input("Gebe deinen Benutzernamen ein:  ")
            passwort = input("Gebe dein Passwort ein: ")
            for kunde in kunden_liste:
                if kunde.benutzername == benutzername and kunde.passwort == passwort:
                    print(f"Herzlichen Willkommen {kunde.name} ")
                    return kunde
            print("Benutzername oder Passwort sind falsch oder nicht gegeben.")
            return einleitung()

        else:
            print("Bitte bestätige mit 1 oder 2")
            return einleitung()

    else:
        print("Bitte gib nur eine Zahl ein, benutze keine Buchstaben")
        return einleitung()

def laden():
    kunden_laden()
    artikel_laden()

einleitung()
laden()
kunden_menue()
