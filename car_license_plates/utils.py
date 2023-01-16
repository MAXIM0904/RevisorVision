from random import choice, randint
import re
from .schema import ListGenerateNumbers

list_letters = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']


def random_number(begin, end, number_characters):
    number = str(randint(begin, end))
    return number.zfill(number_characters)


def creating_numbers(amount):
    list_numbers = []
    for i in range(amount):
        number = f"{choice(list_letters)}{random_number(1, 999, 3)}" \
                 f"{choice(list_letters)}{choice(list_letters)}{random_number(1, 100, 2)}"
        list_numbers.append(number)
    return list_numbers


def number_control(plate):
    pattern = re.compile(r"^[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}")

    if re.fullmatch(pattern, plate):
        return True
    else:
        return False


def response_user(success, numbers):
    return ListGenerateNumbers(
        success=success,
        numbers=numbers
    )
