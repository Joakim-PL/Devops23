def line(dots=False):
    if dots:
        print('*' * 30)
    else:
        print('-' * 30)

def header(text):
    width = 30
    padding = (width - len(text) - 2) // 2
    print('| ' + ' ' * padding + text + ' ' * padding + ' |')

def echo(text):
    print('| ' + text)

def prompt(text):
    user_input = input(f'| {text} >  ')
    return user_input

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')