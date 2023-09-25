teams = {

    'Brazil': {
        'wins': 2,
        'draws': 1,
        'losses': 0,
        'goals for': 5,
        'goals against': 1
    },

    'Serbia': {
        'wins': 1,
        'draws': 0,
        'losses': 2,
        'goals for': 2,
        'goals against': 4
    },
    'Switzerland': {
        'wins': 1,
        'draws': 2,
        'losses': 0,
        'goals for': 5,
        'goals against': 4
    },
    'Costa Rica': {
        'wins': 0,
        'draws': 1,
        'losses': 2,
        'goals for': 2,
        'goals against': 5
    }
}


def make_list(dictionary):
    new_lista = []

    for country in dictionary:
        country_dict = {
            'country': teams[country],
            'wins': teams[country]['wins'],
            'draws': teams[country]['draws'],
            'losses': teams[country]['losses'],
            'goals for': teams[country]['goals for'],
            'goals against': teams[country]['goals against']

        }

        new_lista.append(country_dict)
    return new_lista


my_list = make_list(teams)

summa = 0
for country in my_list:
    summa += country['wins']

print("Summan av alla wins", summa)


def print_table(lista):
    print("-" * 50)
    print("| # | Nation".ljust(11),'|')
    print("-" * 50)
    num = 1
    for i in lista:
        print(F""" | {num} | {i[country].ljust(11)}""")
        num += 1


print_table(my_list)
