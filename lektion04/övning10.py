todos = ['Städa', 'Handla', 'Plugga', 'Ge blod', ]

gissa=input("Ange todo: ")

if gissa in todos:
    print(gissa, "finns i listan")
else:
    print(gissa, "finns inte i listan")
    till=input("Vill du lägga till denna (J/N)? ")

    if 'J' in till:
        print("Todo tillagd!")
        todos.append(gissa)
        todos.sort()
        print(todos)

    else:
        print("Icke tillagd")

