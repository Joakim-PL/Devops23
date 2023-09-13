anteckningar = {
    'Meddelande från skolan': 'Friluftsdag på tisdag',
    'Kom ihåg': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}

print("Lägg till anteckning:")
ny_titel = input("Titel > ")
ny_text = input("Text > ")

anteckningar[ny_titel] = ny_text

for titel, text in anteckningar.items():
    print(f"Titel: {titel}")
    print(f"Text: {text}")
    print("-----")

