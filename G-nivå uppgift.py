import os


class Kortlek:
    def __init__(self):  # hämtar kortlek med färger och kort
        self.farg = ["H", "K", "R", "S"]  # kortfärg,Hjärter,klöver,ruter,spader
        self.kort = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Kn", "D", "K", "E"]
        self.fullt_kortlek = []

        for fargs in self.farg:
            for korts in self.kort:
                self.fullt_kortlek.append(fargs + korts)

    def __str__(self):
        hjarter = []
        klover = []
        ruter = []
        spader = []

        for fargs in self.farg:
            for korts in self.kort:
                if fargs == "H":
                    hjarter.append(fargs + korts)
                elif fargs == "K":
                    klover.append(fargs + korts)
                elif fargs == "R":
                    ruter.append(fargs + korts)
                else:
                    spader.append(fargs + korts)

        return ("Här är hela kortleken: \n\n"
                f"Hjärter: {hjarter}\n"
                f"Klöver: {klover}\n"
                f"Ruter: {ruter}\n"
                f"Spader: {spader}")

    def blanda(self):  # blandar korleken funktion
        kortlek_set = set(self.fullt_kortlek)
        return list(kortlek_set)
