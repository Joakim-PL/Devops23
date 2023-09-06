ui_width = 30

t1 = input("Ange en text: ").lower()
t2 = input("Ange en bokstav: ").lower()
count = 0  # Variabel för att räkna förekomsten av bokstaven t2 i texten t1

print(ui_width * '-')

for i in range(len(t1)):
    if t1[i] == t2:
        count += 1  # Öka räknaren varje gång t2 matchar en bokstav i t1

print(f"Bokstaven {t2} förekommer {count} gånger i texten.")
