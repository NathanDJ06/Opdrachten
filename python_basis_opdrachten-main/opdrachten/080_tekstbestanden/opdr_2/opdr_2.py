# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random


def raad_een_nummertje():
    """Spel waarbij de gebruiker een random getal tussen 1 en 100 moet raden"""

    # Genereer een random getal tussen 1 en 100
    geheime_getal = random.randint(1, 100)
    aantal_pogingen = 0

    print("Raad mijn geheime getal tussen 1 en 100!")

    while True:

        gok = int(input("Raad mijn geheime getal\n"))
        aantal_pogingen += 1


        if gok < geheime_getal:
            print("hoger")
        elif gok > geheime_getal:
            print("lager")
        else:
            print(f"Je hebt het getal geraden het is {geheime_getal}!")
            print(f"Je hebt het in {aantal_pogingen} keer gedaan")
            break


if __name__ == "__main__":
    raad_een_nummertje()
