todos = ['Städa', 'Handla', 'Plugga', 'Ge blod', ]
print(todos[0])
print(todos[1])
print(todos[3])

ny_todo = input("ange en ny todo: ")
todos.append(ny_todo)
print("uppdaterad lista:")
for todo in todos:
    print(todo)