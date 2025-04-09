# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(km):
    return km / 1.609344

def miles_naar_kilometers(miles):
    return miles * 1.609344

# Voorbeeldgebruik
kilometers = 1223
miles = 867

miles_resultaat = kilometers_naar_miles(kilometers)
km_resultaat = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {miles_resultaat} miles")
print(f"{miles} miles = {km_resultaat} kilometers")
