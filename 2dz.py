import math

def calculate_square_root_v1(number):
    if number < 0:
        raise ValueError("Від'ємне число не має дійсного квадратного кореня.")
    return math.sqrt(number)

try:
    number = float(input("Введіть число: "))
    result = calculate_square_root_v1(number)
    print(f"Квадратний корінь з {number} дорівнює {result}.")
except ValueError as e:
    print(f"Помилка: {e}")









def calculate_square_root_v2(number):
    try:
        if number < 0:
            raise ValueError("Від'ємне число не має дійсного квадратного кореня.")
        return math.sqrt(number)
    except ValueError as e:
        return str(e)

number = float(input("Введіть число: "))
result = calculate_square_root_v2(number)
print(result)

