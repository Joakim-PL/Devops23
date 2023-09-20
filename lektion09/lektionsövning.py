class Rectangle:
    length = 0
    width = 0

    def area(self):
        return self.length * self.width


r1 = Rectangle()
r1.width = 5
r1.length = 10
print("Area", r1.area())
r1.omkrets = r1.width * 2 + r1.length * 2
print("Omkrets", r1.omkrets)

def omkrets(self1):
    return self1.width * 2 + self1.length * 2

o1 = omkrets()
o1.width = 5
o1.length = 10
print(o1.omkrets())