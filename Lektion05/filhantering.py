import os

if os.path.exists('textfil.txt'):
    # Öppna en befintlig fil r betyder read
    f = open('textfil.txt', 'r')
else:
    # Skapa en ny fil x betyder create
    f = open('textfil.txt', 'x')

with open('textfil.txt', 'a+') as myFile:
    myFile.write("Rad 4\n")
    myFile.seek(0)
    text = myFile.read()
