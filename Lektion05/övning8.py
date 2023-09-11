heltal_forekomst = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

with open('numbers.csv', 'r') as file:
    for line in file:
        heltal = int(line.strip())
        heltal_forekomst[heltal] += 1

print("-" * 15 + " NUMANALYZER " + "-" * 15)
for heltal in range(10):
    antal_forekomst = heltal_forekomst[heltal]
    print(f"| {heltal} | {antal_forekomst}")
print("-" * 39)
