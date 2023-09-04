ui_width = 30

print(ui_width * '*')
print(ui_width * '-')
print('.: Mathlete v2.0 :.'.center(ui_width))
print('-' * ui_width)

nummer_lista = []

while True:
    inmatning = input("Mata in ett nummer > ")

    if inmatning.lower() == 'exit':
        break

    try:
        nummer = float(inmatning)
        nummer_lista.append(nummer)
    except ValueError:
        print("Ogiltig inmatning")

if nummer_lista:
    print('-' * ui_width)
    print("Kardinalitet:", len(nummer_lista))
    print("Summa", sum(nummer_lista))
    print("Medelvärdet", sum(nummer_lista) / len(nummer_lista))
