import random


class Kortlek:
    def __init__(self):
        self.farger = ["Hjärter", "Klöver", "Ruter", "Spader"]  # kortens färger
        self.varden = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Kn", "D", "K", "E"]  # lista för kortleken
        self.korts = []  # listan innehåller korten i kortleken
        self.spelare_hand = []  # lista med spelarens kort
        self.dator_hand = []  # lista med datorns kort

    def skapa_kortlek(self):  # skapar kortleken med värden och kortens färger t.ex klöver
        self.korts = [(farg, vard) for farg in self.farger for vard in self.varden]

    def blanda_kortlek(self):  # blandar kortleken
        random.shuffle(self.korts)

    def dela_kort(self):  # delar ut kortleken
        return self.korts.pop()

    def calculate_points(self, hand, card_values):  # funktion som räknar poängen
        total_value = 0  # innehåller den totala poängen
        num_aces = 0  # antalet ess

        for farg, vard in hand:
            total_value += card_values[vard]

        for farg, vard in hand:  # räknar antalet ess
            if vard == 'E':
                num_aces += 1

        while num_aces > 0 and total_value < 8:  # funktion som klarar av att själv bestämma om ess ska vara 1 eller 14
            total_value += 14
            num_aces -= 1

        for farg, vard in hand:
            if vard == 'E':
                while True:
                    ess_value = input("Vill du att Ess ska vara 1 eller 14? ").strip()
                    if ess_value in ["1", "14"]:  # Låter användaren välja om ess ska vara 1 eller 14
                        card_values['E'] = int(ess_value)
                        break
                    else:
                        print("Vänligen välj antingen 1 eller 14.")

        return total_value  # returnerar den totala poängen

    def spela_spelet(self):  # funktion styr hela spelet
        card_values = {  # Kortvärden för både spelaren och datorn
            '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10, 'Kn': 11, 'D': 12,
            'K': 13, 'E': 14  # Standardvärde för ess
        }

        while True:
            # delar ut kort till både spelaren och datorn
            self.spelare_hand.append(self.dela_kort())
            self.dator_hand.append(self.dela_kort())

            print("=" * 40)
            print("Välkommen till Tjugioett".center(40))  # simpelt ui i spelet
            print("=" * 40)
            print("Din hand:")

            for farg, vard in self.spelare_hand:
                print(f"{vard} av {farg}")

            spelare_value = self.calculate_points(self.spelare_hand, card_values)  # räknar ut spelarens hand
            print(f"Totalt värde av din hand: {spelare_value}")

            if spelare_value > 21:  # spelaren förlorar om den överstiger 21
                print("Du har förlorat.")
                break

            till_kort = input("Vill du ta ett till kort? (ja/nej): ").strip().lower()
            if till_kort != "ja":  # om svaret inte är ja så bryts loopen
                break

        while self.calculate_points(self.dator_hand, card_values) < 17:  # datorn tar nytt kort om den är under 17
            self.dator_hand.append(self.dela_kort())

        print("Datorns hand:")
        for farg, vard in self.dator_hand:
            print(f"{vard} av {farg}")

        dator_value = self.calculate_points(self.dator_hand, card_values)  # räknar ut datorns poäng
        print(f"Totalt värde av datorns hand: {dator_value}")

        # om datorn får mer än 21 så vinner spelaren, om spelaren får mer än datorn men under 21 så vinner spelaren
        if dator_value > 21 or spelare_value > dator_value:
            print("Grattis! Du vinner!")
        elif dator_value > spelare_value:  # datorn vinner om den har mer än spelaren
            print("Datorn vinner.")
        else:
            print("Det är oavgjort!")

        self.spelare_hand = []  # nollställer spelet till nästa runda
        self.dator_hand = []
        self.korts = []


if __name__ == "__main__":  # huvudspelet
    kortlek = Kortlek()
    while True:
        kortlek.skapa_kortlek()
        kortlek.blanda_kortlek()
        kortlek.spela_spelet()
        cont = input("Vill du spela igen ja/nej: ").strip().lower()
        if cont != "ja":  # om svaret inte är ja så bryts loopen
            break
