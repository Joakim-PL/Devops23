multi = int(input("Ange multiplikationstabell > "))
tal = 0
while True:
    tal += multi
    print(tal)
    tal += multi
    print(tal)
    tal += multi
    print(tal)
    cont = input("Fortsätt? ")
    if cont == "ja":
        continue
    else:
        break