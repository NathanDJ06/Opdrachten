# Opdracht 1 functies
# Naam student:
# Groep:


def volledige_naam(lijst_met_namen):
    for persoon in lijst_met_namen:
        # Voeg onderdelen samen, en verwijder lege strings
        onderdelen = [persoon["voornaam"], persoon["tussenvoegsel"], persoon["achternaam"]]
        naam = " ".join(deel for deel in onderdelen if deel)
        print(naam)

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)
