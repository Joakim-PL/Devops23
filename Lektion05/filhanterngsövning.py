attendants = ['Lisa', 'Kalle', 'Olivia', 'Johan']

with open('textfil.txt', 'w') as f:
    for attendant in attendants:
        f.write('Hello ' + attendant + '!\n')
