största = float('-inf')  # Ett mycket litet startvärde för att säkerställa att det första inmatade talet blir största
lägsta = float('inf')   # Ett mycket stort startvärde för att säkerställa att det första inmatade talet blir lägsta
summa = 0
antal_tal = 0

while True:
    try:
        tal = float(input("Mata in ett tal: "))
        if tal < 0:
            break  # Avsluta loopen om användaren matar in ett negativt tal
        else:
            antal_tal += 1
            summa += tal
            if tal > största:
                största = tal
            if tal < lägsta:
                lägsta = tal
    except ValueError:
        print("Ogiltig inmatning. Försök igen.")

if antal_tal > 0:
    medelvärde = summa / antal_tal
    print("--------------------------")
    print("Största inmatade tal:", största)
    print("Lägsta inmatade tal:", lägsta)
    print("Summan av inmatade tal:", summa)
    print("Medelvärdet av inmatade tal:", medelvärde)
else:
    print("Inga giltiga tal matades in.")
