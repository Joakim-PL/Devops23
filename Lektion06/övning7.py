anteckningar = {
    'Meddelande från skolan': 'Friluftsdag på tisdag',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}

ui_width = 30

print(".: ALWAYSNOTE :.".center(ui_width))
print("-- gold edition --".center(ui_width))
print("*" * ui_width)
print("- Meddelande från skolan")
print("- Kom ihåg!")
print("- Inför tentamen")
print("-" * 30)
print("View | view note")
print("Add | add note")
print("RM | remove note")
print("Exit | exit program")
print("-" * 30)

while True:
    menu = input("Menu > ")

    if menu == 'view'.lower():
        for titel, text in anteckningar.items():
            print(f"Titel: {titel}")
            print(f"Text: {text}")
            print("-----")

    elif menu == 'add'.lower():
        print("Add note:")
        ny_titel = input("Titel > ")
        ny_text = input("Text > ")

        anteckningar[ny_titel] = ny_text

        for titel, text in anteckningar.items():
            print(f"Titel: {titel}")
            print(f"Text: {text}")
            print("-----")

    elif menu == 'RM'.lower():
        while True:
            tabort = input("Remove note: ").lower()
            if tabort in anteckningar:
                del anteckningar[tabort]
                for titel, text in anteckningar.items():
                    print(f"Titel: {titel}")
                    print(f"Text: {text}")
                    print("-----")
                break
            else:
                print("That doesn't exist")

    elif menu == 'exit'.lower():
        break
print("Exiting program....")
print("＞︿＜")





