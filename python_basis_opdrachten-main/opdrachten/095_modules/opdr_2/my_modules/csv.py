#!/usr/bin/env python3
# Dit is de module
# In dit bestand komen alle functies.
# Je kunt de functies in een ander .py bestand gebruiken door te starten  met:
# from my_modules import csv

# my_modules/csv.py

def read_csv(filename):
    """Leest een CSV bestand en retourneert de gegevens als lijst van dictionaries"""
    with open(filename, 'r') as file:
        headers = file.readline().strip().split(',')
        data = []
        for line in file:
            values = line.strip().split(',')
            data.append(dict(zip(headers, values)))
    return data

def write_csv(filename, data):
    """Schrijft data naar een CSV bestand"""
    with open(filename, 'w') as file:
        if data:
            headers = data[0].keys()
            file.write(','.join(headers) + '\n')
            for row in data:
                file.write(','.join(str(row[header]) for header in headers) + '\n')

def filter(data, filterveld, filter):
    """Filtert de lijst op basis van beginletters van een veld"""
    filtered = []
    for persoon in data:
        if persoon[filterveld].lower().startswith(filter.lower()):
            filtered.append(persoon)
    return filtered

def print_personen(data):
    """Print personen in een leesbaar formaat"""
    for persoon in data:
        print(f"{persoon['voornaam']} {persoon['achternaam']}")