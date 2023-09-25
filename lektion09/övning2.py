class Circle:
    def __init__(self, radie):
        self.radie = radie
        self.pi = 3.14

    def rakna(self):
        omkrets = 2 * self.pi * self.radie
        return omkrets


cirkel = Circle(3)

omkrets = cirkel.rakna()

print("Omkrets:", omkrets)
