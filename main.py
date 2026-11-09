# ===== T-1. Главное меню (общая задача) =====
TITLE = "Касса кофейни"  # впишите название своего продукта
MENU = []  # пункты меню: (название, функция)


def ask_int(text):
    # спрашивает целое число, пока его не введут правильно
    while True:
        value = input(text).strip()
        if value.lstrip("-").isdigit():
            return int(value)
        print("Ошибка: введите целое число")


def ask_float(text):
    # спрашивает число (можно дробное), пока его не введут правильно
    while True:
        value = input(text).strip().replace(",", ".")
        try:
            return float(value)
        except ValueError:
            print("Ошибка: введите число")


def start():
    while True:
        print()
        print("=====", TITLE, "=====")
        for number, item in enumerate(MENU, start=1):
            print(number, "-", item[0])
        print("0 - Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "0":
            print("До свидания!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(MENU):
            MENU[int(choice) - 1][1]()
        else:
            print("Нет такого пункта меню")


# ===== US-2. Меню напитков =====
DRINKS = [
    ("Эспрессо", 120),
    ("Американо", 150),
    ("Капучино", 200),
    ("Латте", 220),
    ("Раф", 250),
    ("Какао", 180),
]


def show_drinks():
    for number, (name, price) in enumerate(DRINKS, start=1):
        print(f"{number}. {name} — {price} руб.")


MENU.append(("Меню напитков", show_drinks))


# ===== ЗАПУСК: эта строка всегда должна быть последней =====
start()
