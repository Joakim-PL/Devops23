ui_width = 30
print("Robber translate")
print(ui_width * '-')

konsonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

sv = input("Mata in en text: ")

oversatt = ""

for tecken in sv:
    omvandlat = tecken
    omvandlat = omvandlat.lower()

    if omvandlat in konsonant:
        omvandlat += 'o'

    oversatt += omvandlat

print("Rövarspråk", oversatt)
