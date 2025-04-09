# Opdracht 1 functies
# Naam student:
# Groep:


from my_modules import csv


if __name__ == "__main__":

    data = [
        ["Naam", "Leeftijd", "Stad"],
        ["Alice", 28, "Amsterdam"],
        ["Bob", 35, "Rotterdam"],
        ["Charlie", 42, "Utrecht"]
    ]

    # Schrijf naar CSV
    csv.write_csv("personen.csv", data)
    print("Bestand geschreven naar personen.csv")

    # Lees van CSV
    gelezen_data = csv.read_csv("personen.csv")
    print("\nInhoud van het CSV-bestand:")
    csv.print_csv(gelezen_data)