def minimun(lista):
    minsta_talet = lista[0]
    for i in lista:
        if minsta_talet > i:
            minsta_talet = i

    print(minsta_talet)


def greet(first_name, last_name):
    print("Hello", first_name, last_name)


greet("Lisa", "Svensson")
mylist = [2, 5, 7, 4, 9]
minimun(mylist)
