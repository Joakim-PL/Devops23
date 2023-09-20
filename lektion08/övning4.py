import random

def get_even(lst):
    even_numbers = [x for x in lst if x % 2 == 0]
    return even_numbers

numbers = []
for x in range(10):
    numbers.append(random.randint(0, 9))

even = get_even(numbers)
print('even:', even)
print('numbers:', numbers)
