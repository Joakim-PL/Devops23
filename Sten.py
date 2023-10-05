import random
import os
import sys

ui_width = 40

# FUNKTION FÖR VÄLKOMNANDE *******
def get_username():
    if os.path.exists('username.txt'):
        with open('username.txt', 'r') as f:
            return f.read()
# *********************************

class RockPaperScissor:

    def __init__(self):
        self.options = ["sten", "sax", "påse"]
        self.user_score = 0  # players score
        self.computer_score = 0  # computers score

    def play(self):
        while True:
            self.clear_screen()
            self.spel()

    def clear_screen(self):  # clear terminal
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    # EXIT FUNKTION *********
    def exit_game(self):
        return True
    # ************************

    def spel(self):  # the game and ui
        print("=" * 40)
        print(f"|  .:Välkommen {get_username()} till sten, sax, påse:.  |".center(ui_width))
        print("=" * 40)
        print(f"| Poäng - Utmanare: {self.user_score} | Datorn: {self.computer_score} |".center(40))
        print("| Försten till 3 vinner! |".center(ui_width))
        print("-" * 40)
        players_choice = input("| Välj sten, sax eller påse: ").lower()
        print("-" * 40)

        if players_choice not in self.options:  # controll if the players choice is valid
            print("Ogiltig inmatning, Vänligen försök igen.")
            return

        computer_choice = random.choice(self.options)  # computers choice is randomized

        print(f"| Du valde {players_choice}. Datorn valde {computer_choice}.")

        if players_choice == computer_choice:
            print("| Det blev oavgjort.")
        elif (players_choice == "sten" and computer_choice == "sax") or \
                (players_choice == "sax" and computer_choice == "påse") or \
                (players_choice == "påse" and computer_choice == "sten"):  # and, or funktion to decide who won the game
            print("| Du vann")
            self.user_score += 1  # The player earn a point every time the player wins

        else:
            print("| Datorn vann")
            self.computer_score += 1  # The computer also earns points

        if self.computer_score == 3:  # the game ends if the player loses to the computer
            self.clear_screen()
            print("=" * 40)
            print("|  .:Välkommen till sten, sax, påse:.  |".center(ui_width))
            print("=" * 40)
            print(f"| Poäng - Utmanare: {self.user_score} | Datorn: {self.computer_score} |".center(40))
            print("| Datorn vann. Spelet är slut. |".center(40))

        elif self.user_score == 3:  # the game ends if the player wins over the computer
            self.clear_screen()
            print("=" * 40)
            print("|  .:Välkommen till sten, sax, påse:.  |".center(ui_width))
            print("=" * 40)
            print(f"| Poäng - Utmanare: {self.user_score} | Datorn: {self.computer_score} |".center(40))
            print("| Grattis du vann. Spelet är slut. |".center(40))


if __name__ == "__main__":  # main program
    game = RockPaperScissor()
    while True:

        game.clear_screen()
        game.spel()
        print("-" * 40)
        if game.user_score == 3:
            cont = input("| Vill du spela igen (ja/nej): ").strip().lower()

            while cont not in ["ja", "nej"]:  # Error message if ja/nej is not answered
                print("| Ogiltig inmatning. Vänligen svara med 'ja' eller 'nej'.")
                cont = input("| Vill du spela igen (ja/nej): ").strip().lower()

            if cont == "nej":  # exiting the game
                if game.exit_game():
                    # print("| Tack för att du ville spela") *********
                    print("| Tack för att du ville spela")
                    break

        elif game.computer_score == 3:
            cont = input("| Vill du spela igen (ja/nej): ").strip().lower()

            while cont not in ["ja", "nej"]:  # Error message if ja/nej is not answered
                print("| Ogiltig inmatning. Vänligen svara med 'ja' eller 'nej'.")
                cont = input("| Vill du spela igen (ja/nej): ").strip().lower()

            if cont == "nej":  # exiting the game
                if game.exit_game():
                    # print("| Tack för att du ville spela") *********
                    print("| Tack för att du ville spela")
                    break



