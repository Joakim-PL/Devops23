import os

if os.name == 'nt':
    os.system('cls')
    print('Du kör Windows')
elif os.name == 'posix':
    os.system('clear')
    print('Du kör Mac eller Linux')
