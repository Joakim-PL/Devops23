kända_personer = {
    "Daniel Radcliffe": {"Kön": "man", "Hårfärg": "brun", "Ögonfärg": "brun"},
    "Rupert Grint": {"Kön": "man", "Hårfärg": "röd", "Ögonfärg": "blå"},
    "Emma Watson": {"Kön": "kvinna", "Hårfärg": "brun", "Ögonfärg": "brun"},
    "Selena Gomez": {"Kön": "kvinna", "Hårfärg": "brun", "Ögonfärg": "brun"},
}

kön = input("Ange kön: ").lower()
hårfärg = input("Ange hårfärg: ").lower()
ögonfärg = input("Ange ögonfärg: ").lower()

matchade_personer = [kön,hårfärg,ögonfärg]

if matchade_personer[kön,hårfärg,ögonfärg] in kända_personer:
    print("Egenskaperna matchar med:"(kända_personer))
          
else:
    print("Ingen känd person matchar med egenskaperna.")

