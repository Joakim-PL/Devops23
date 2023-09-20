ui_width = 30

space = ui_width - 2
text = 'Exempel'.center(space)

ui_line = "|" + text + "|"

print("-" * ui_width)
print(ui_line)
print("*" * ui_width)
print("|","Detta är ett exempel på hur\n| ett grännsitt kan se ut.")
print("-" * ui_width)

space = ui_width - 2
text2 = '..vad vill du göra?'.center(space)
ui_line2 = "|" + text2 + "|"

print(ui_line2)
print("-" * ui_width)

print("| A | Visa inköpslista")
print("| B | Lägg till vara ")
print("| C | Ta bort vara")
print("| X | Stäng programmet")
print("-" * ui_width)
print("| Val >")
