person = {
    "firstname": "Johan",
    "lastname": "Svensson",
    "age": 25,
    "pets": [
        {"name": "Morris", "age": 3, "type": "dog"},
        {"name": "Lisa", "age": 2, "type": "cat"}
    ]
}

namn = person["firstname"] + " " + person["lastname"]
age = person['age']
pets = person['pets']
count_pets = len(pets)

print(f"{namn} är {age} år gammal och har {count_pets} husdjur:")

for pet in pets:
    print(f"* En {pet['age']} år gammal {pet['type']} som heter {pet['name']} ")
