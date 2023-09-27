import random
import os

ui_width = 40


class RockPaperScissor:
    def __init__(self):
        self.options = ["sten", "sax", "påse"]

    def clear_screen(self):  # clear terminal
        os.system('cls' if os.name == 'nt' else 'clear')

    def spel(self):  # the game and ui
        self.clear_screen()
        print("\033c")  # ANSI escape-sequence to clear the screen
        print("-" * 40)
        print("|  .:Välkommen till sten, sax, påse:.  |".center(ui_width))
        print("-" * 40)
        players_choice = input("| Välj sten, sax eller påse: ").lower()

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

        else:
            print("| Datorn vann")


if __name__ == "__main__":
    game = RockPaperScissor()
    while True:
        game.spel()
        print("-" * 40)
        cont = input("| Vill du spela igen (ja/nej): ").lower()
        if cont == "ja":
            continue
        else:
            break
