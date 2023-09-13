anteckningar = {

'Meddelande från skolan': 'titel 1',
'Kom ihåg!': 'titel 2',
'inför tentamen': 'titel 3'
}
print(".: ANTECKNINGAR :.")
print("*" * 30)

for titel in anteckningar.keys():
    print(f"- {titel}")
