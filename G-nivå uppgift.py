import random


class Hand:
    def __init__(self):
        self.korts = []

    def add_card(self, card):
        self.korts.append(card)

    def calculate_points(self):
        points = 0  # räknar ut poängen i spelet
        esser = 0  # Räknar ut hur många ess som finns i spelarens hand

        for kort in self.korts:  # ger Ess, Kn, D och K deras kortvärden
            if kort == "E":
                points += 14
                esser += 1
            elif kort in ["Kn"]:
                points += 11
            elif kort in ["D"]:
                points += 12
            elif kort in ["K"]:
                points += 13
            else:
                points += int(kort)

        while points > 21 and esser > 0:  # points kollar om spelaren har gått över 21,E kollar om det finns E att räkna
            points -= 14  # gör så att om spelaren får ett till E så överstiger inte 21
            esser -= 1  # används för att hålla koll på oanvända ess

        return points


class Kortlek:
    def __init__(self):
        self.farger = ["H", "K", "R", "S"]  # hjärter, klöver, ruter och spader
        self.varden = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Kn", "D", "K", "E"]
        self.korts = []

    def skapa_kortlek(self):  # skapar kortleken med värden och kortens färger t.ex klöver
        self.korts = [farg + vard for farg in self.farger for vard in self.varden]

    def blanda_kortlek(self):
        random.shuffle(self.korts)  # blandar kortleken

    def dela_kort(self):
        return self.korts.pop()  # delar ut korten


def spel():
    spelares_hand = Hand()
    datorns_hand = Hand()
    kortlek = Kortlek()

    print("=" * 40)
    print("Välkommen".center(40))
    print("Spelet Tjugoett".center(40))
    print("Målet är att komma så nära 21 som möjligt".center(40))
    print("Lycka till!".center(40))

    kortlek.skapa_kortlek()
    kortlek.blanda_kortlek()

    for _ in range(2):
        spelares_hand.add_card(kortlek.dela_kort())  # ge spelaren två kort från kortleken
        datorns_hand.add_card(kortlek.dela_kort())  # ge datorn två kort från kortleken

    while True:
        spelar_val = input("Vill du dra ett kort? (ja/nej): ").strip().lower()

        if spelar_val == "ja":
            spelares_hand.add_card(kortlek.dela_kort())  # lägger till ett kort i spelarens hand
            print(f"Du drog: {spelares_hand.korts[-1]}")  # ger spelaren det sista kortet i listan
            spelar_poang = spelares_hand.calculate_points()  # räknar ut spelarens poäng
            print(f"Dina poäng: {spelar_poang}\n")

            if spelar_poang == 21:  # om spelaren vinner
                print("Grattis! Du fick 21 poäng. Du vinner!")
                break

            elif spelar_poang > 21:  # om spelaren överstiger 21 så förlorar man
                print("Du fick över 21 poäng. Du förlorar!")
                break

        elif spelar_val == "nej":
            break
        else:
            print("Ogiltig inmatning")

    if spelar_val == "ja":
        while datorns_hand.calculate_points():  # räkna ut datorns hand
            datorns_hand.add_card(kortlek.dela_kort())  # lägger till ett kort till datorn
            print(f"Datorn drog: {datorns_hand.korts[-1]}")  # ger datorn sista kortet i listan

        datorn_poang = datorns_hand.calculate_points()  # datorns poäng
        print(f"\nDatorns poäng: {datorn_poang}\n")
