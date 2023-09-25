class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        person_info = f"{self.name} är {self.age} år och bor på adressen {self.address}."
        return person_info


person_name = 'Joakim'
person_age = '18'
person_address = 'Indalsbacken'

person = Person(person_name, person_age, person_address)
person_description = person.info()

print(person_description)
