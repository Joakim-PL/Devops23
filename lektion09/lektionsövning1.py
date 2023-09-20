from random import randint


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
r1 = Rectangle(5, 10)

r_list = []

summa = 0
for i in range(0, 1000):
    r_list.append(Rectangle(randint(1, 100), randint(1, 100)))
print(r_list)