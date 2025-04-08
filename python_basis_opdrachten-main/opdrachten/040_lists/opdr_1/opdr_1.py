# Opdracht 1 lists
# Naam student: Nathan de Jong
# Groep: IT2A

lijst = []

dict_1 = { "id": 0, "naam": "Nathan", "achternaam": "Heitbrink" }
dict_2 = { "id": 1, "naam": "Kevin", "achternaam": "Samson" }
dict_3 = { "id": 2, "naam": "Jasper", "achternaam": "Boonestroo" }
dict_4 = { "id": 3, "naam": "Olav", "achternaam": "de_Jong" }

lijst.extend([dict_1, dict_2, dict_3, dict_4])

print(lijst[1]["naam"], lijst[1]["achternaam"])
