todos = ['Städa', 'Handla', 'Plugga', 'Ge blod', ]
print(todos[0])
print(todos[1])
print(todos[3])

tabort = input("Ta bort en todo: ")

if tabort in todos:
    todos.remove(tabort)
    print(tabort, "har tagits bort")

todos.sort()

print("uppdaterad lista:")
for todosa in todos:
    print(todosa)

ny_todo = input("ange en ny todo: ")
todos.append(ny_todo)
todos.sort()

print(ny_todo, "Har lagts till")
print("uppdaterad lista:")
todos.sort()
for todo in todos:
    print(todo)

gissa = input("Ange todo: ")

if gissa in todos:
    print(gissa, "finns i listan")
else:
    print(gissa, "finns inte i listan")
    till = input("Vill du lägga till denna (J/N)? ")

    if 'J' in till:
        print("Todo tillagd!")
        todos.append(gissa)
        todos.sort()
        print(todos)

    else:
        print("Icke tillagd")
