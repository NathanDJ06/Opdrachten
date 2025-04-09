# Opdracht 1 modules
# Naam student:
# Groep:

# opdr_1.py
from my_modules import csv


def main():
    # Voorbeeld data
    personen = [
        {"voornaam": "Jan", "achternaam": "Van Der Vliet", "plaats": "Amsterdam"},
        {"voornaam": "Piet", "achternaam": "De Vries", "plaats": "Den Haag"},
        {"voornaam": "Griet", "achternaam": "Van Der Pol", "plaats": "Delft"},
        {"voornaam": "Jan Jaap", "achternaam": "Siewers", "plaats": "Dordrecht"}
    ]

    # Schrijf naar CSV
    csv.write_csv("personen.csv", personen)

    # Lees van CSV
    gelezen_data = csv.read_csv("personen.csv")

    # Voorbeelden van filteren
    print("\nPersonen met voornaam die begint met 'Ja':")
    gefilterd = csv.filter(gelezen_data, "voornaam", "Ja")
    csv.print_personen(gefilterd)

    print("\nPersonen met voornaam die begint met 'Pie':")
    gefilterd = csv.filter(gelezen_data, "voornaam", "Pie")
    csv.print_personen(gefilterd)

    print("\nPersonen uit plaatsen die beginnen met 'D':")
    gefilterd = csv.filter(gelezen_data, "plaats", "d")
    csv.print_personen(gefilterd)


if __name__ == "__main__":
    main()