# Opdracht 3 condities
# Naam student:
# Groep:




# Hier komt je code...

normale_toegangsprijs = 12.50
kortings_percentages = {
    "baby": 100,
    "kinderen": 50,
    "volwassenen": 0,
    "ouderen": 30
}
leeftijdsgroepen = {
    "baby": (0, 2),
    "kinderen": (3, 18),
    "volwassenen": (19, 64),
    "ouderen": (65, 150)
}

leeftijd = int(input("Geef uw leeftijd in aantal jaar\n"))


for groep, (min_leeftijd, max_leeftijd) in leeftijdsgroepen.items():
    if min_leeftijd <= leeftijd <= max_leeftijd:
        korting = kortings_percentages[groep]
        prijs = normale_toegangsprijs * (1 - korting / 100)
        print(f"U behoort tot de groep {groep}")
        print(f"U krijgt {korting}% korting")
        print(f"U betaalt daarom {prijs:.2f}")
        break
