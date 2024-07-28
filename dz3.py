def main():
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

    def display_menu():
        print("\nМеню:")
        print("1. Відображення словника")
        print("2. Пошук значення в словнику")
        print("3. Заміна значення в словнику")
        print("4. Відображення значення за ключем")
        print("5. Видалення значення за ключем")
        print("6. Вихід")

    def execute_option(user_dict):
        while True:
            display_menu()
            option = input("Виберіть опцію (1-6): ")

            if option == '1':
                print("\nСловник:", user_dict)

            elif option == '2':
                key = input("Введіть ключ для пошуку значення: ")
                try:
                    print(f"Значення за ключем '{key}': {user_dict[key]}")
                except KeyError:
                    print("Помилка: Ключ не знайдено.")

            elif option == '3':
                key = input("Введіть ключ для заміни значення: ")
                if key in user_dict:
                    new_value = input("Введіть нове значення: ")
                    user_dict[key] = new_value
                    print(f"Значення за ключем '{key}' змінено.")
                else:
                    print("Помилка: Ключ не знайдено.")

            elif option == '4':
                key = input("Введіть ключ для відображення значення: ")
                try:
                    print(f"Значення за ключем '{key}': {user_dict[key]}")
                except KeyError:
                    print("Помилка: Ключ не знайдено.")

            elif option == '5':
                key = input("Введіть ключ для видалення значення: ")
                try:
                    del user_dict[key]
                    print(f"Значення за ключем '{key}' видалено.")
                except KeyError:
                    print("Помилка: Ключ не знайдено.")

            elif option == '6':
                print("Вихід з програми.")
                break

            else:
                print("Невірний вибір. Будь ласка, виберіть опцію від 1 до 6.")

    user_dict = fill_dictionary()
    execute_option(user_dict)

if __name__ == "__main__":
    main()
