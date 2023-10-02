import random

class Hand:
    def __init__(self):
        self.korts = []

    def add_card(self, card):
        self.korts.append(card)

    def calculate_score(self):
        score = 0
        esser = 0

        for kort in self.korts:
            if kort == "E":
                score += 14
                esser += 1
            elif kort in ["Kn", "D", "K"]:
                score += 10
            else:
                score += int(kort)

        while score > 21 and esser > 0:
            score -= 14
            esser -= 1

        return score

class Kortlek:
    def __init__(self):
        self.farger = ["H", "K", "R", "S"]
        self.varden = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Kn", "D", "K", "E"]
        self.korts = []

    def skapa_kortlek(self):
        self.korts = [farg + vard for farg in self.farger for vard in self.varden]

    def blanda_kortlek(self):
        random.shuffle(self.korts)

    def dela_kort(self):
        return self.korts.pop()

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
