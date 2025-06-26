import datetime

liste0000000000kunden = []
liste0000000000artikel = []
liste0000000000korb = []
liste0000000000orders = []


def menue0000000000start():
    print("09090909202009090909")
    funktion00000000testdaten()
    while True:
        print("\n1. Kundenmenü")
        print("2. Artikelmenü")
        print("3. Warenkorb")
        print("4. Bestellung")
        print("5. Berichte")
        print("0. Beenden")
        eingabe00000000menue = input("> ")
        if eingabe00000000menue == "1":
            menue0000000000kunden()
        elif eingabe00000000menue == "2":
            menue0000000000artikel()
        elif eingabe00000000menue == "3":
            menue0000000000korb()
        elif eingabe00000000menue == "4":
            funktion00000000bestellen()
        elif eingabe00000000menue == "5":
            funktion00000000berichte()
        elif eingabe00000000menue == "0":
            break


def menue0000000000kunden():
    print("09090909202009090909")
    print("\n1. Kunde hinzufügen")
    print("2. Kunden anzeigen")
    print("3. Kunde löschen")
    print("4. Kunde suchen")
    eingabe00000000kunde = input("> ")
    if eingabe00000000kunde == "1":
        name = input("Name: ")
        adresse = input("Adresse: ")
        liste0000000000kunden.append({"nummer": len(liste0000000000kunden)+1, "name": name, "adresse": adresse})
    elif eingabe00000000kunde == "2":
        for kunde in liste0000000000kunden:
            print(kunde)
    elif eingabe00000000kunde == "3":
        nummer = int(input("Kundennummer: "))
        liste0000000000kunden[:] = [k for k in liste0000000000kunden if k["nummer"] != nummer]
    elif eingabe00000000kunde == "4":
        name = input("Name: ")
        for k in liste0000000000kunden:
            if name in k["name"]:
                print(k)


def menue0000000000artikel():
    print("09090909202009090909")
    print("\n1. Artikel erstellen")
    print("2. Artikel anzeigen")
    print("3. Artikel löschen")
    print("4. Artikel suchen")
    eingabe00000000artikel = input("> ")
    if eingabe00000000artikel == "1":
        titel = input("Titel: ")
        beschreibung = input("Beschreibung: ")
        preis = float(input("Preis: "))
        bestand = int(input("Lagerbestand: "))
        kategorie = input("Kategorie: ")
        liste0000000000artikel.append({"id": len(liste0000000000artikel)+1, "titel": titel, "beschreibung": beschreibung, "preis": preis, "bestand": bestand, "kategorie": kategorie})
    elif eingabe00000000artikel == "2":
        for a in liste0000000000artikel:
            print(a)
    elif eingabe00000000artikel == "3":
        id = int(input("Artikel-ID: "))
        liste0000000000artikel[:] = [a for a in liste0000000000artikel if a["id"] != id]
    elif eingabe00000000artikel == "4":
        suchbegriff = input("Suchbegriff: ")
        for a in liste0000000000artikel:
            if suchbegriff.lower() in a["titel"].lower():
                print(a)


def menue0000000000korb():
    print("09090909202009090909")
    print("\n1. Artikel hinzufügen")
    print("2. Artikel entfernen")
    print("3. Warenkorb anzeigen")
    print("4. Gesamt berechnen")
    eingabe00000000korb = input("> ")
    if eingabe00000000korb == "1":
        id = int(input("Artikel-ID: "))
        menge = int(input("Menge: "))
        liste0000000000korb.append({"id": id, "menge": menge})
    elif eingabe00000000korb == "2":
        id = int(input("Artikel-ID entfernen: "))
        liste0000000000korb[:] = [k for k in liste0000000000korb if k["id"] != id]
    elif eingabe00000000korb == "3":
        for k in liste0000000000korb:
            print(k)
    elif eingabe00000000korb == "4":
        summe = 0
        for k in liste0000000000korb:
            artikel = next((a for a in liste0000000000artikel if a["id"] == k["id"]), None)
            if artikel:
                summe += artikel["preis"] * k["menge"]
        print("Gesamtbetrag:", summe)


def funktion00000000bestellen():
    print("09090909202009090909")
    kunde = input("Kundenname: ")
    adresse = input("Adresse: ")
    bestellung = {"kunde": kunde, "adresse": adresse, "datum": datetime.date.today(), "positionen": liste0000000000korb[:], "gesamt": 0}
    summe = 0
    for k in liste0000000000korb:
        artikel = next((a for a in liste0000000000artikel if a["id"] == k["id"]), None)
        if artikel:
            summe += artikel["preis"] * k["menge"]
            artikel["bestand"] -= k["menge"]
    bestellung["gesamt"] = summe
    liste0000000000orders.append(bestellung)
    liste0000000000korb.clear()
    print("\nBestellung abgeschlossen.")


def funktion00000000berichte():
    print("09090909202009090909")
    print("\n1. Bestellanzahl")
    print("2. Gesamtumsatz")
    print("3. Umsatz nach Artikel")
    eingabe00000000bericht = input("> ")
    if eingabe00000000bericht == "1":
        print("Anzahl Bestellungen:", len(liste0000000000orders))
    elif eingabe00000000bericht == "2":
        print("Gesamtumsatz:", sum(b["gesamt"] for b in liste0000000000orders))
    elif eingabe00000000bericht == "3":
        artikelumsatz = {}
        for b in liste0000000000orders:
            for p in b["positionen"]:
                a = next((x for x in liste0000000000artikel if x["id"] == p["id"]), None)
                if a:
                    artikelumsatz[a["titel"]] = artikelumsatz.get(a["titel"], 0) + a["preis"] * p["menge"]
        for titel, umsatz in sorted(artikelumsatz.items(), key=lambda x: x[1], reverse=True):
            print(f"{titel}: {umsatz}")


def funktion00000000testdaten():
    print("09090909202009090909")
    liste0000000000artikel.append({"id": 1, "titel": "HTW T-Shirt", "beschreibung": "Weißes Shirt mit Logo", "preis": 19.99, "bestand": 20, "kategorie": "Kleidung"})
    liste0000000000artikel.append({"id": 2, "titel": "HTW Becher", "beschreibung": "Keramikbecher", "preis": 9.99, "bestand": 15, "kategorie": "Zubehör"})
    liste0000000000kunden.append({"nummer": 1, "name": "Max Mustermann", "adresse": "Musterweg 1, 66111 Saarbrücken"})
    liste0000000000korb.append({"id": 1, "menge": 2})
    liste0000000000korb.append({"id": 2, "menge": 1})
    print("Testdaten geladen.")


menue0000000000start()