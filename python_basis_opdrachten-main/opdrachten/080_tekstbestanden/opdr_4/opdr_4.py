# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


def party_organisatie():
    """Vraagt feestgangers naar hun bijdrage en slaat deze op"""

    # Lijst met vragen
    vragen = [
        "Wat is je voornaam?",
        "Wat is je achternaam?",
        "Wat neem je mee aan drank?",
        "Wat neem je mee om te eten?"
    ]

    # Toon welkomstbericht
    print("Welkom bij de party organisatie!")
    print("Vul alstublieft deze korte vragenlijst in:\n")

    # Dictionary voor antwoorden
    antwoorden = {}

    # Stel alle vragen en sla antwoorden op
    for i, vraag in enumerate(vragen, 1):
        print(f"{i}. {vragen[i - 1]}")
        antwoord = input()
        sleutel = vragen[i - 1].split()[-1].replace("?", "").lower()
        antwoorden[sleutel] = antwoord

    # Bedankbericht
    print("\nBedankt voor het invullen!")
    print("See you at the party.\n")

    # Sla antwoorden op in bestand
    with open("feestgangers.txt", "a") as bestand:
        for key, value in antwoorden.items():
            bestand.write(f"{key}: {value}\n")
        bestand.write("\n")  # Lege regel tussen verschillende gasten


def hoofdmenu():
    """Hoofdmenu voor party organisatie"""
    while True:
        print("\nParty Organisatie Menu")
        print("1. Nieuwe feestganger toevoegen")
        print("2. Afsluiten")
        keuze = input("Maak een keuze (1/2): ")

        if keuze == "1":
            party_organisatie()
        elif keuze == "2":
            print("Programma afgesloten. Tot op de party!")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw")


if __name__ == "__main__":
    hoofdmenu()