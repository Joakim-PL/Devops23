import os

POST_1 = ''
POST_2 = ''
POST_3 = ''

while True:
    if os.name == 'nt':
        os.system('cls')
        print('Du kör Windows')
    elif os.name == 'posix':
        os.system('clear')
        print('Du kör Mac eller Linux')

    print('.: basicBILLBOARD :. ')
    print(' ******************** ')
    print('P1:', POST_1)
    print('P2:', POST_2)
    print('P3:', POST_3)
    print(' --------------------')
    print('c | Ändra post ')
    print('e | Stäng program ')
    print(' --------------------')

    val = input("Välj ett kommando: ").lower()

    if val == 'c':
        post_nr = input("Vilken post vill du ändra?").upper()
        inneholl = input("Ange det nya innehållet: ")

        if post_nr == 'P1':
            POST_1 = inneholl
        elif post_nr == 'P2':
            POST_2 = inneholl
        elif post_nr == 'P3':
            POST_3 = inneholl
        else:
            print("Ogiltig postnummer. Välj P1, P2 eller P3.")

    elif val == 'e':
        break
    else:
        print("Ogiltigt kommando.")

    input("Tryck enter för att fortsätta ... ")
