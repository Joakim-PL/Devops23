import os


def create_sign(message):
    sign_width = 50
    border = "|" + "-" * (sign_width - 2) + "|"
    message_lines = message.splitlines()
    max_line_length = max(len(line) for line in message_lines)

    print(border)
    for line in message_lines:
        padding = (max_line_length - len(line)) // 2
        left_padding = " " * padding
        right_padding = " " * (max_line_length - len(line) - padding)
        print(f"| {left_padding}{line}{right_padding} |")

    print(border)


def change_sign_message():
    new_message = input("Ange det nya meddelandet: ")
    with open('sign.txt', 'w') as sign_file:
        sign_file.write(new_message)


if not os.path.exists('sign.txt'):
    initial_message = "Welcome to Västerås"
    with open('sign.txt', 'w') as sign_file:
        sign_file.write(initial_message)
else:
    with open('sign.txt', 'r') as sign_file:
        initial_message = sign_file.read()

while True:
    create_sign(initial_message)
    print("C | Change sign message")
    print("E | Exit program")
    print("-" * 50)
    choice = input("> ").upper()

    if choice == 'C':
        change_sign_message()
    elif choice == 'E':
        break
    else:
        print("Ogiltigt val. Försök igen.")
