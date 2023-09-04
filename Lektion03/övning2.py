namn=input("Ange namn: ")
alder=int(input("Ange ålder: "))

if alder == '1':
    print("Hej!",namn,"du ska sova 14 timmar per dag")

elif alder == '2':
    print("Hej!",namn,"du ska sova 13 timmar per dag")

elif alder == '3':
    print("Hej!",namn,"du ska sova 12 timmar per dag")

elif alder == '4':
    print("Hej!",namn,"du ska sova 11,5 timmar per dag")

elif alder in range (5,6):
    print("Hej!",namn,"du ska sova 11 timmar per dag")

elif alder == '7':
    print("Hej!",namn,"du ska sova 10,5 timmar per dag")

elif alder in range (8,10):
    print("Hej!",namn,"du ska sova 10 timmar per dag")

elif alder == '11':
    print("Hej!",namn,"du ska sova 9,5 timmar per dag")

elif alder in range (12,15):
    print("Hej!",namn,"du ska sova 9 timmar per dag")

elif alder == '16':
    print("Hej!",namn,"du ska sova 8,5 timmar per dag")

elif alder in range (17,100):
    print("Hej!",namn,"du ska sova 8 timmar per dag")

