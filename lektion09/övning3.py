import os
class BankAccount:
    def __init__(self, saldo, bankonto):
        self.saldo = saldo
        self.bankonto = bankonto

    def get_bankonto(self):
        nummer = self.bankonto()
        return nummer

    def get_saldo(self):
        pengar = self.saldo()
        return pengar


ui_width = 30
nummer = 123123123
pengar = 10000
kontonummer = 23232323

print("-" * 30)
print("Bankonto")
print("SEB")
print(nummer)
while True:
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

    st = input("Vill du gå in i ditt bankonto y/n > ")
    try:
        if st == 'Y'.lower():
            print("-" * 30)
            print("Kontonummer ", kontonummer)
            print("Saldo", pengar, "Kr")
            inut = input("Vill du vilja göra insättning eller uttag i/u > ")

            if inut == 'I'.lower():
                print("-" * 30)
                print("Insättning")
                print(pengar, "Kr")
                intag = int(input("Ange belopp för insättning > "))
                intag += pengar
                print("-" * 30)
                print("Saldot:", pengar)

            elif inut == 'U'.lower():
                print("-" * 30)
                print("Uttag")
                print(pengar, "Kr")
                uttag = int(input("Ange belopp för uttag > "))
                if uttag > pengar:
                    print("Du har inte tillräckligt med pengar!")
                else:
                    pengar -= uttag
                    print("-" * 30)
                    print("Saldot:", pengar)
                    print("Uttag:", uttag)

            else:
                print("Ogiltig inmatning")

        elif st == 'N'.lower():
            print("Vänligen vänta...")
            print("Avslutas")
            break

        else:
            print("Ogiltig inmatning")

    except KeyError:
        print("Ogiltig inmatning")
