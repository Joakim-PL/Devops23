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
menu = input("MENU > ")

if menu == 'Push':
    print()
