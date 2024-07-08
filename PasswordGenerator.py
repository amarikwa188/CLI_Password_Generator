import random
from string import ascii_lowercase, ascii_uppercase
from itertools import cycle


def randomize(string: str) -> str:
    """
    Randomize the order of characters in a string.\n
    :param string: original string input\n
    :return: random string permutation
    """
    new = [x for x in string]
    random.shuffle(new)
    return ''.join(new)


def generator(length: int, upper: bool, lower: bool, numbers: bool, symbols: bool) -> str:
    """
    Generate a random password.\n
    :param length: length of password
    :param upper: True -> password will contain uppercase chars 
    :param lower: True -> password will contain lowercase chars
    :param number: True -> password will contain numbers
    :param symbols: True -> password will contain symbols\n
    :return: generated password
    """
    pool: list[str] = list()
    pool.append(ascii_uppercase if upper else None)
    pool.append(ascii_lowercase if lower else None)
    pool.append('0123456789' if numbers else None)
    pool.append('!@$%&?/'if symbols else None)
    pool = [char_type for char_type in pool if char_type]
    draw = cycle(pool)

    password: str = ''
    for _ in range(length):
        current: str = next(draw)
        password += current[random.randint(0, len(current)-1)]

    return randomize(password)


if __name__ == '__main__':
    info: dict[str: int | bool | None] = {'length': None, 'upper': None, 'lower': None, 'numbers': None, 'symbols': None}
    while True:
        try:
            pass_length: int = int(input("Enter password length:\n>").strip())
        except ValueError:
            print("Invalid length. Enter a number.\n")
        else:
            info['length'] = pass_length
            break

    while True:
        up: str = input("Contain uppercase?(True/False):\n>").lower().strip()
        if up not in ('true', 'false'):
            print("Invalid input. Enter 'True' or 'False'.\n")
        else:
            info['upper'] = True if up == 'true' else False
            break

    while True:
        low: str = input("Contain lowercase?(True/False):\n>").lower().strip()
        if low not in ('true', 'false'):
            print("Invalid input. Enter 'True' or 'False'.\n")
        else:
            info['lower'] = True if low == 'true' else False
            break

    while True:
        nums: str = input("Contain numbers?(True/False):\n>").lower().strip()
        if nums not in ('true', 'false'):
            print("Invalid input. Enter 'True' or 'False'.\n")
        else:
            info['numbers'] = True if nums == 'true' else False
            break

    while True:
        symbol: str = input("Contain symbols?(True/False):\n>").lower().strip()
        if symbol not in ('true', 'false'):
            print("Invalid input. Enter 'True' or 'False'.\n")
        else:
            info['symbols'] = True if symbol == 'true' else False
            break

    print(f"\nPassword: {generator(**info)}")
