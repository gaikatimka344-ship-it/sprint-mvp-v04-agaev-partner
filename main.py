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


# ===== US-3. Добавить напиток в заказ =====
order = []  # позиции заказа: (напиток, цена, количество)


def add_to_order():
    show_drinks()
    number = ask_int("Номер напитка: ")
    if number < 1 or number > len(DRINKS):
        print("Нет такого напитка")
        return
    count = ask_int("Количество: ")
    if count <= 0:
        print("Количество должно быть больше 0")
        return
    name, price = DRINKS[number - 1]
    order.append((name, price, count))
    print(f"Добавлено: {name} x {count}")


MENU.append(("Добавить в заказ", add_to_order))


# ===== US-4. Сумма заказа =====
def order_sum():
    total = 0
    for name, price, count in order:
        total = total + price * count
    return total


def show_order_sum():
    if len(order) == 0:
        print("Заказ пуст")
        return
    for name, price, count in order:
        print(f"{name} x {count} = {price * count} руб.")
    print(f"Итого: {order_sum()} руб.")


MENU.append(("Сумма заказа", show_order_sum))


# ===== US-5. К оплате со скидкой =====
def pay_with_discount():
    total = order_sum()
    if total >= 500:
        discount = total * 0.1
        print(f"Сумма: {total} руб., скидка 10 %: {discount:.2f} руб.")
        total = total - discount
    else:
        print("Скидка 10 % действует при заказе от 500 руб.")
    print(f"К оплате: {total:.2f} руб.")


MENU.append(("К оплате (со скидкой)", pay_with_discount))


# ===== ЗАПУСК: эта строка всегда должна быть последней =====
start()
