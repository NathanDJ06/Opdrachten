# Opdracht 2 lists
# Naam student: Nathan de Jong
# Groep: IT2A


rivier_info = {
    "Rijn": ["Nederland", "Duitsland", "Frankrijk"],
    "Maas": ["Nederland", "België", "Duitsland"],
    "Nijl": ["Egypte", "Soedan", "Oeganda"]
}

rivieren = list(rivier_info.keys())

# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

info1 = (rivier_info["Rijn"][1])
info2 = (rivieren[0])
print(f"De rivier {info2} stroomt onder andere door {info1}")
#De rivier Rijn stroomt onder andere door Duitsland
info1 = (rivier_info["Maas"][0])
info2 = (rivieren[1])
print(f"De rivier {info2} stroomt onder andere door {info1}")\
#De rivier Maas stroomt onder andere door Nederland
info1 = (rivier_info["Nijl"][2])
info2 = (rivieren[2])
print(f"De rivier {info2} stroomt onder andere door {info1}")
#De rivier Nijl stroomt onder andere door Oeganda