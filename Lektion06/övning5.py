anteckningar = {
    'Meddelande från skolan': 'Friluftsdag på tisdag',
    'Kom ihåg': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}

tabort = input("Ta bort anteckning: ").lower()
if tabort in anteckningar:
    del anteckningar[tabort]
    for titel, text in anteckningar.items():
        print(f"Titel: {titel}")
        print(f"Text: {text}")
        print("-----")

else:
    print("Fel inmatning")

