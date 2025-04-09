# Opdracht 1 functies
# Naam student:
# Groep:


import math

def kubus_vol(zijde):
    return zijde ** 3

def bol_vol(straal):
    return (4/3) * math.pi * (straal ** 3)

# Voorbeeldgebruik
volume_kubus = kubus_vol(5)
volume_bol = bol_vol(4)

print(f"De inhoud van deze kubus is: {volume_kubus}")
print(f"De inhoud van deze bol is: {volume_bol}")
