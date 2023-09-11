person = {

    "name": "Joakim",
    "age": 18
}

#Hämta element

print(person)
print(str(person['age']))

#Referera nyckel dynamiskt
'''
attr = input("Ange Nyckel > ")

try:
    print(person[attr])
except KeyError as fel:
    print("Fel! nyckel existerar inte")
    print("Du skrev: " + str(fel))
'''

#ändra värdet
person['age'] = 19
print(person)

#Lägga till nya data, key value pair
person["address"] = "Indalsbacken"
print(person)

#tabort element

del person ['age']
print(person)

#kopiera
person_copy = person.copy()
print(person_copy)

del (person_copy)

# iteration av dict
for key in person:
    print("key",key)
    print("value",person[key])

#Nästlande dict
person["address"] = {
    "gatuaddress": "Indalsbacken",
    "ort": "Vällingby",
    "postnummer": "16268"
}
#adressen svensk standard
print(person['address']['gatuaddress'])
print(person['address']['postnummer'], (person['address']['ORT']).upper())


