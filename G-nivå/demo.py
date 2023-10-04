import random


class Hand:
    def __init__(self):
        self.korts = []

    def add_card(self, card):
        self.korts.append(card)

    def calculate_points(self, hand):
        total_value = 0
        num_aces = 0

        for suit, value in hand:
            if value in 'Knäckt':
                total_value += 11
            elif value in 'Dam':
                total_value += 12
            if value in 'Kung':
                total_value += 13
            elif value == 'Ess':
                num_aces += 1
                total_value += 1
            else:
                total_value += int(value)

        for _ in range(num_aces):
            if total_value <= 11:
                total_value += 13
            else:
                total_value += 1

        return total_value


class Kortlek:
    def __init__(self):
        self.farger = ["Hjärter", "Klöver", "Ruter", "Spader"]  # kort färger
        self.varden = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Kn", "D", "K", "E"]
        self.korts = []

    def skapa_kortlek(self):  # skapar kortleken med värden och kortens färger t.ex klöver
        self.korts = [(farg, vard) for farg in self.farger for vard in self.varden]

    def blanda_kortlek(self):
        random.shuffle(self.korts)  # blandar kortleken

    def dela_kort(self):
        return self.korts.pop()  # delar ut korten

    def spel(self):
        while True:
            print("\nDin hand:")
            for suit, value in self.player_hand:
                print(f"{value} av {suit}")
            player_value = self.calculate_hand_value(self.player_hand)
            print(f"Totalt värde av din hand: {player_value}")

            if player_value == 21:
                print("Grattis! Du har Blackjack!")
                break
            elif player_value > 21:
                print("Du är tjock! Du förlorar.")
                break

            action = input("\nVill du ta ett till kort? (ja/nej): ").lower()
            if action == "ja":
                self.player_hand.append(self.deck.draw_card())
            else:
                break

        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.draw_card())

        print("\nDealerns hand:")
        for suit, value in self.dealer_hand:
            print(f"{value} av {suit}")
        dealer_value = self.calculate_hand_value(self.dealer_hand)
        print(f"Totalt värde av dealerns hand: {dealer_value}")

        if dealer_value > 21 or player_value > dealer_value:
            print("Grattis! Du vinner!")
        elif dealer_value > player_value:
            print("Dealern vinner.")
        else:
            print("Det är oavgjort!")


if __name__ == "__main__":
    while True:
        spel()
        cont = input("Vill du spela igen ja/nej: ").strip().lower()
        if cont != "ja":
            break
