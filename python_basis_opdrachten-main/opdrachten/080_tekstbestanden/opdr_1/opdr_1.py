# Opdracht 1 while-loops
# Naam student:
# Groep:

# opdr_1.py

def voer_enquete_uit():
    """Voert een korte enquête uit en slaat de resultaten op"""

    print("Bedankt voor het deelnemen aan deze korte enquête!\n")

    # Stel de vragen
    vragen = [
        "Wat vind je van de huidige regering? ",
        "Wat vind je van de Python-lessen tot nu toe? ",
        "Wat vind jij de mooiste stad van Nederland? "
    ]

    antwoorden = []

    for vraag in vragen:
        antwoord = input(vraag)
        antwoorden.append(antwoord)

    # Sla de resultaten op
    with open("enquete_resultaten.txt", "a") as bestand:
        bestand.write("=== Nieuwe enquête resultaten ===\n")
        for i in range(len(vragen)):
            bestand.write(f"Vraag {i + 1}: {vragen[i]}\n")
            bestand.write(f"Antwoord: {antwoorden[i]}\n\n")

    print("\nBedankt voor je deelname! Je antwoorden zijn opgeslagen.")


if __name__ == "__main__":
    voer_enquete_uit()