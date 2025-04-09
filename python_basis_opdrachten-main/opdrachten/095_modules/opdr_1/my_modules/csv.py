# my_modules/csv.py

def read_csv(filename):
    """Leest een CSV bestand en retourneert de gegevens als lijst van rijen"""
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))
    return data

def write_csv(filename, data):
    """Schrijft data naar een CSV bestand"""
    with open(filename, 'w') as file:
        for row in data:
            file.write(','.join(str(item) for item in row) + '\n')

def print_csv(data):
    """Print CSV data netjes geformatteerd"""
    for row in data:
        print(" | ".join(str(item) for item in row))