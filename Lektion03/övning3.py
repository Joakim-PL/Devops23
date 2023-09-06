import random

while True:

    dice = random.randint(1, 6)

    if dice == 1:
        print("Du slog en 1:a")
        print(" -------")
        print("|       |")
        print("|   •   |")
        print("|       |")
        print(" -------")

    elif dice == 2:
        print("Du slog en 2:a")
        print(" -------")
        print("| •     |")
        print("|       |")
        print("|     • |")
        print(" -------")

    elif dice == 3:
        print("Du slog en 3:a")
        print(" -------")
        print("| •     |")
        print("|   •   |")
        print("|     • |")
        print(" -------")

    elif dice == 4:
        print("Du slog en 4:a")
        print(" -------")
        print("| •   • |")
        print("|       |")
        print("| •   • |")
        print(" -------")

    elif dice == 5:
        print("De slog en 5:a")
        print(" -------")
        print("| •   • |")
        print("|   •   |")
        print("| •   • |")
        print(" -------")

    elif dice == 6:
        print("Du slog en 6:a")
        print(" -------")
        print("| •   • |")
        print("| •   • |")
        print("| •   • |")
        print(" -------")

    spelaigen = input("Vill du spela igen (y/n): ")
    if spelaigen == 'yes':
        break
