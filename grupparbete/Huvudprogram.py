from Wordguess import WordGuessingGame, clear_terminal
from Sten import RockPaperScissor
import GoFish
import Hang

def main():
    while True:
        # Skriv ut menyn.
        clear_terminal()
        print("Välj ett spel:")
        print("1. Ordgissaren")
        print("2. Sten, Sax, Påse")
        print("3. Finns i Sjön")
        print("4. Hängagubbe")

        # Läs in användarens val.
        game_choice = input("Välj ett spel > ")

        # Starta spelet om användaren väljer "Ordgissaren".
        if game_choice == "1":
            WordGuessingGame()
        elif game_choice == "2":
            game = RockPaperScissor()
            game.play()
        elif game_choice == "3":
            GoFish.main_game()
        elif game_choice == "4":
            Hang.main()
        elif game_choice == "no":
            break


if __name__ == "__main__":
    main()