with open('database.csv', 'r') as file:
    lines = file.readlines()

header = lines[0].strip().split(',')
people_data = []

for line in lines[1:]:
    person = line.strip().split(',')
    person_data = dict(zip(header, person))
    people_data.append(person_data)


    def search_by_gender():
        search_gender = input("Ange kön (M/F): ").strip().upper()
        found = False

        for person in people_data:
            if person['GENDER'].strip().upper() == search_gender:
                found = True
                print("Hittad person:")
                for key, value in person.items():
                    print(f"{key}: {value}")

        if not found:
            print(f"Ingen person med kön {search_gender} hittades.")

    def search_by_year():
        search_year = input("Ange födelseår: ").strip()
        found = False

        for person in people_data:
            if person['YEAR'].strip() == search_year:
                found = True
                print("Hittad person:")
                for key, value in person.items():
                    print(f"{key}: {value}")

        if not found:
            print(f"Ingen person med födelseår {search_year} hittades.")

def search_name():
    search_name = input("Ange för- eller efternamn för sökning: ").strip().lower()
    found = False

    for person in people_data:
        if search_name in person['FORENAME'].strip().lower() or search_name in person['SURNAME'].strip().lower():
            found = True
            print(f"Hittad person med namnet '{search_name}':")
            for key, value in person.items():
                print(f"{key}: {value}")

    if not found:
        print(f"Ingen person med namnet '{search_name}' hittades.")

while True:
    print("\nVälj ett alternativ:")
    print("1. Sök efter person med kön")
    print("2. Sök efter person med födelseår")
    print("3. Sök efter person med för- eller efternamn")
    print("4. Avsluta programmet")

    choice = input("Ange ditt val (1/2/3/4): ")

    if choice == '1':
        search_by_gender()
    elif choice == '2':
        search_by_year()
    elif choice == '3':
        search_name()
    elif choice == '4':
        print("Programmet avslutas.")
        break
    else:
        print("Ogiltigt val. Försök igen.")
