def palindrom(mening):
    renad_mening = "".join(mening.split()).lower()
    return renad_mening == renad_mening[::-1]


ui_width = 30
print("Palindrom-testare")
print(ui_width * '-')

input_mening = input("Ange en mening: ")

if palindrom(input_mening):
    print(f"' {input_mening} ' är ett palindrom")
else:
    print(f"' {input_mening} ' är inte ett palindrom")
