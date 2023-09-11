from sys import exit

ui_width = 30
print(".: STACKMASTER v1.33.7 :.".center(ui_width))
print("-" * ui_width)

bilar = ['Mercedes', 'Volvo', 'Toyota']

for bila in bilar:
    print("-", bila)

print("-" * ui_width)
print("| MENU |".center(ui_width))
print("-" * ui_width)

print("Push | push element to stack")
print("Pull | pull element from stack")
print("Exit | exit program")
print("-" * ui_width)

while True:
    menu = input("MENU > ")

    if menu == 'Push':
        print("Push element to stack")
        nybil = input("Element to push to the stack: ")
        bilar.append(nybil)
        for bila in bilar:
            print("-", bila)

    elif menu == 'Pull':
        print("Pull element from stack")
        tabil = input("State the element from stack: ")
        if tabil in bilar:
            bilar.remove(tabil)
            for bila in bilar:
                print("-", bila)
        else:
            print(f"'{tabil}' was not found in the stack.")

    elif menu == 'Exit':
        exit()

    else:
        print("Wrong input")
        break
