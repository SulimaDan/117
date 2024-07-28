import math

def calculate_square_root():
    try:
        number = float(input("Введіть число: "))
        if number < 0:
            raise ValueError("Від'ємне число не має дійсного квадратного кореня.")
        square_root = math.sqrt(number)
        print(f"Квадратний корінь з {number} дорівнює {square_root}.")
    except ValueError as e:
        print(f"Помилка: {e}")

calculate_square_root()
