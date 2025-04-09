# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

def caesar_cipher(tekst, verschuiving=5, encrypt=True):
    """
    Versleutel of ontcijfer tekst met Caesar cipher methode
    :param tekst: de invoertekst
    :param verschuiving: aantal posities om te verschuiven (standaard 5)
    :param encrypt: True voor encryptie, False voor decryptie
    :return: versleutelde of ontcijferde tekst
    """
    resultaat = []

    for karakter in tekst:
        if karakter.isalpha():
            # Bepaal basis voor hoofdletters of kleine letters
            basis = ord('A') if karakter.isupper() else ord('a')
            # Bereken nieuwe karakterpositie
            if encrypt:
                nieuwe_pos = (ord(karakter) - basis + verschuiving) % 26
            else:
                nieuwe_pos = (ord(karakter) - basis - verschuiving) % 26
            nieuw_karakter = chr(basis + nieuwe_pos)
            resultaat.append(nieuw_karakter)
        else:
            # Behoud niet-alfabetische karakters
            resultaat.append(karakter)

    return ''.join(resultaat)


def main():
    print("Tekst encryptie/decryptie programma")
    print("1. Encrypten")
    print("2. Decrypten")
    keuze = input("Maak een keuze (1/2): ")

    tekst = input("Geef de tekst die je wilt bewerken:\n")

    if keuze == '1':
        versleuteld = caesar_cipher(tekst)
        print("\nVersleutelde tekst:")
        print(versleuteld)
    elif keuze == '2':
        ontcijferd = caesar_cipher(tekst, encrypt=False)
        print("\nOntcijferde tekst:")
        print(ontcijferd)
    else:
        print("Ongeldige keuze")


if __name__ == "__main__":
    main()

