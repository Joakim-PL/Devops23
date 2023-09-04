tal = input("Mata in ett heltal > ")
try:
    tal = int(tal)
    svar = tal * 2
    print(svar, "är ditt svar")

except ValueError:
    print(tal, "är inte ett heltal")
