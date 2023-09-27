import random
import os

ui_width = 40


class RockPaperScissor:
    def __init__(self):
        self.options = ["sten", "sax", "påse"]
        self.life = 3

    def clear_screen(self):  # clear terminal
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def spel(self):  # the game and ui
        print("-" * 40)
        print("|  .:Välkommen till sten, sax, påse!:.  |".center(ui_width))
        print(f"| Du har {self.life} liv |".center(ui_width))
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
            self.life -= 1  # The player loses a life when computer wins

        print(f"| du har {self.life} liv kvar.")

        if self.life == 0:  # If the player have no lifes left the game ends
            print("| Du har inga liv kvar. Spelet är slut.")
            exit()


if __name__ == "__main__":
    game = RockPaperScissor()
    clear = RockPaperScissor()
    while True:
        clear.clear_screen()
        game.spel()
        print("-" * 40)
        cont = input("| Vill du spela igen (ja/nej): ").strip().lower()

        try:
            if cont == "ja":
                continue
            elif cont == "nej":
                break
            else:
                raise ValueError  # stop if the answer is not ja/nej

        except ValueError:
            print("| Ogiltig inmatning. Vänligen svara med 'ja' eller 'nej'.")


