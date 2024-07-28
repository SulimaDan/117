def fill_dictionary():
    user_dict = {}
    print("Введіть пари 'ключ/значення' для заповнення словника. Введіть 'stop' для завершення.")
    while True:
        key = input("Введіть ключ: ")
        if key.lower() == 'stop':
            break
        value = input("Введіть значення: ")
        if value.lower() == 'stop':
            break
        user_dict[key] = value
    return user_dict

def display_dictionary(user_dict):
    print("\nСловник:", user_dict)

def search_value(user_dict, key):
    return user_dict[key]

def replace_value(user_dict, key, new_value):
    user_dict[key] = new_value

def get_value(user_dict, key):
    return user_dict[key]

def delete_value(user_dict, key):
    del user_dict[key]

def main_v1():
    user_dict = fill_dictionary()
    
    while True:
        print("\nМеню:")
        print("1. Відображення словника")
        print("2. Пошук значення в словнику")
        print("3. Заміна значення в словнику")
        print("4. Відображення значення за ключем")
        print("5. Видалення значення за ключем")
        print("6. Вихід")
        
        option = input("Виберіть опцію (1-6): ")

        if option == '1':
            display_dictionary(user_dict)

        elif option == '2':
            key = input("Введіть ключ для пошуку значення: ")
            try:
                value = search_value(user_dict, key)
                print(f"Значення за ключем '{key}': {value}")
            except KeyError:
                print("Помилка: Ключ не знайдено.")

        elif option == '3':
            key = input("Введіть ключ для заміни значення: ")
            try:
                new_value = input("Введіть нове значення: ")
                replace_value(user_dict, key, new_value)
                print(f"Значення за ключем '{key}' змінено.")
            except KeyError:
                print("Помилка: Ключ не знайдено.")

        elif option == '4':
            key = input("Введіть ключ для відображення значення: ")
            try:
                value = get_value(user_dict, key)
                print(f"Значення за ключем '{key}': {value}")
            except KeyError:
                print("Помилка: Ключ не знайдено.")

        elif option == '5':
            key = input("Введіть ключ для видалення значення: ")
            try:
                delete_value(user_dict, key)
                print(f"Значення за ключем '{key}' видалено.")
            except KeyError:
                print("Помилка: Ключ не знайдено.")

        elif option == '6':
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір. Будь ласка, виберіть опцію від 1 до 6.")

if __name__ == "__main__":
    main_v1()














def fill_dictionary():
    user_dict = {}
    print("Введіть пари 'ключ/значення' для заповнення словника. Введіть 'stop' для завершення.")
    while True:
        key = input("Введіть ключ: ")
        if key.lower() == 'stop':
            break
        value = input("Введіть значення: ")
        if value.lower() == 'stop':
            break
        user_dict[key] = value
    return user_dict

def display_dictionary(user_dict):
    print("\nСловник:", user_dict)

def search_value(user_dict, key):
    try:
        return user_dict[key]
    except KeyError:
        return "Помилка: Ключ не знайдено."

def replace_value(user_dict, key, new_value):
    try:
        user_dict[key] = new_value
        return f"Значення за ключем '{key}' змінено."
    except KeyError:
        return "Помилка: Ключ не знайдено."

def get_value(user_dict, key):
    try:
        return user_dict[key]
    except KeyError:
        return "Помилка: Ключ не знайдено."

def delete_value(user_dict, key):
    try:
        del user_dict[key]
        return f"Значення за ключем '{key}' видалено."
    except KeyError:
        return "Помилка: Ключ не знайдено."

def main_v2():
    user_dict = fill_dictionary()
    
    while True:
        print("\nМеню:")
        print("1. Відображення словника")
        print("2. Пошук значення в словнику")
        print("3. Заміна значення в словнику")
        print("4. Відображення значення за ключем")
        print("5. Видалення значення за ключем")
        print("6. Вихід")
        
        option = input("Виберіть опцію (1-6): ")

        if option == '1':
            display_dictionary(user_dict)

        elif option == '2':
            key = input("Введіть ключ для пошуку значення: ")
            result = search_value(user_dict, key)
            print(result)

        elif option == '3':
            key = input("Введіть ключ для заміни значення: ")
            new_value = input("Введіть нове значення: ")
            result = replace_value(user_dict, key, new_value)
            print(result)

        elif option == '4':
            key = input("Введіть ключ для відображення значення: ")
            result = get_value(user_dict, key)
            print(result)

        elif option == '5':
            key = input("Введіть ключ для видалення значення: ")
            result = delete_value(user_dict, key)
            print(result)

        elif option == '6':
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір. Будь ласка, виберіть опцію від 1 до 6.")

if __name__ == "__main__":
    main_v2()
