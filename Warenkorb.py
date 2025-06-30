import csv
import datetime
artikel_liste = [] #Liste mit allen Artikeln
kunden_liste = [] # Liste mit allen Kunden
warenkorb = [] # Temporärer Warenkorb
bestellungen = []
#Rabatte
rabatt_aktiv = False
rabatt_Prozent = 10
min_bestellwert = 50.0

class Kunde:
    def __init__(self,id,name,benutzername,passwort,plz,strasse,ort):
        self.id = id
        self.name = name
        self.benutzername = benutzername
        self.passwort = passwort
        self.plz = plz
        self.strasse = strasse
        self.ort = ort

def kunden_speichern(dateiname="kunden.csv"):
    with open(dateiname,mode="w", encoding="utf-8") as k_liste:
        writer=csv.writer(k_liste)
        writer.writerow(["ID", "Name","Benutzername", "Passwort", "Strasse","PLZ", "Ort"])
        for kunde in kunden_liste:
            writer.writerow([kunde.id, kunde.name,kunde.benutzername, kunde.passwort, kunde.strasse, kunde.plz, kunde.ort])

def kunden_laden(dateiname="kunden.csv"):
    with open(dateiname,mode= "r", encoding="utf-8") as k_liste:
        reader= csv.reader(k_liste)
        next(reader)             #Die erste Zeile wird übersprungen da dort keine echten kundendaten stehen.
        for row in reader:
            if len(row) == 7:
                id,name,benutzername,passwort,strasse,plz,ort = row
                kunden_liste.append(Kunde(int(id),name,benutzername, passwort, strasse, plz, ort))

def einleitung():
    kunden_laden()
    print("Sind sie aktueller Kunde ?")
    member = int(input("1. Ja  / 2. Nein "))

    if member == 2:
        print("Bitte legen Sie ein Benutzerkonto an.")
        name = input("Name: ")
        benutzername = input("Benutzername: ")
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

einleitung()

#Menü für kunden
def kunden_menue():
    while True:
        print("\n--- WI Fanshop ---")
        print("1. Artikel suchen")
        print("2. Artikel anzeigen")
        print("3. Artikel in Warenkorb")
        print("4. Warenkorb anzeigen")
        print("5. Bestellung abschließen")
        print("9. Verwaltung")
        print("0. Abbrechen")
        auswahl = input()

        if auswahl == "1": artikel_suchen()
        elif auswahl == "2": artikel_anzeigen()
        elif auswahl == "3": artikel_in_warenkorb()
        elif auswahl == "4": warenkorb_anzeigen()
        elif auswahl == "5": warenkorb_bestellen()
        elif auswahl == "9": admin_menue()
        elif auswahl == "0": break
        else: print("Auswahl ungültig")
kunden_menue()

#Menü für die Betreiber/Admins
def verwaltungs_menue():
    while True:
        print("\n--- Webshop Verwaltung ---")
        print("1. Artikel hinzufügen")
        print("2. Artikel löschen")
        print("3. Artikel bearbeiten")
        print("4. Rabatt Aktivieren")
        print("5. Bericht Anzeigen")
        print("6. Kunden liste")
        print("0. Abbrechen")
        auswahl = input()

        if auswahl == "1": artikel_hinzufügen()
        elif auswahl == "2": artikel_loeschen()
        elif auswahl == "3": artikel_bearbeiten()
        elif auswahl == "4": rabatt_aktivieren()
        elif auswahl == "5": bericht_anzeigen()
        elif auswahl == "6": kunden_liste()
        elif auswahl == "0": break
        else: print("Auswahl ungültig")