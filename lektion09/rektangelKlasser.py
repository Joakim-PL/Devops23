# Demo om klasser

class Rectangle:
    def __int__(self, length, width):
        self.__length = length
        self.__width = width

    #attribut


   def get_length(self):
       return self.__length

   def set_length(self, length):
       self.__length = length

   def get_width(self):
       return self.__width
   #metoder
    def area(self):
        return self.length * self.width


# skapa objekt av klassen Rectangle
r1 = Rectangle(1, 2)
print(r1.__width)
print(r1.get_length)

#ändra attribut

r1.width = 5
r1.length = 10

print(r1.width)
print(r1.length)

print("Area", r1.area())

r2 = Rectangle(2, 3)
r2.width = 10
r2.length = 10
print("Area", r2.area())
