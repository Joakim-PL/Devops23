ui_width = 30

print(ui_width * '*')
print(ui_width * '-')
print('The Great Divider'.center(ui_width))
print('Beräkna c för uttrycket:'.center(ui_width))
print('a / b = c'.center(ui_width))
print('-' * ui_width)

talA = input("Mata in för A > ")
talB = input("Mata in för B > ")
print('-' * ui_width)

try:
    talA = float(talA)
    talB = float(talB)

    if talA == 0:
        print("FEL! a = 0.")
    elif talB == 0:
        print("FEL! b = 0.")
    else:
        talc = talA / talB
        print(talA, "/", talB, "=", talc)

except ValueError:
    print("Ogiltig inmatning")


