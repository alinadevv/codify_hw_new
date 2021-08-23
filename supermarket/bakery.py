products = (
    {"id": 1, "name": "Вишневый пирог", "price": 35},
    {"id": 2, "name": "Маковый кекс", "price": 85},
    {"id": 3, "name": "Банан в шоколаде", "price": 50},
    {"id": 4, "name": "Тройной Twix", "price": 125},
    {"id": 5, "name": "Булочка с малиной", "price": 77}
)

divider1 = ('♥♡' * 30)

denial = ("Такой товар отсутствует!")

purchase_basket = []

user_money = int()


def main():
    global user_money
    user_money = None
    while user_money == None:
        try:
            user_money = float(input('Введите количество ваших наличных средств: '))
            if user_money <= 0:
                user_money = None
                raise Exception('Недостаточное количество средств для похода в супермаркет!')
            else:
                options()
        except ValueError:
            print('Неверный формат ввода!')
            main()
        except Exception as e:
            print(e)
            main()


def options():
    print(divider1)
    print('''Добро пожаловать в раздел "Выпечка и сладости"!
        Выберите опцию что Вы хотите сделать: 
        1. Посмотреть весь список товаров. 
        2. Найти товар по имени.
        3. Добавить товар в корзину. 
        4. Очистить корзину.
        5. Посмотреть список продуктов в корзине.
        6. Удалить определенный элемент из корзины.
        7. Посмотреть денежный баланс.
        8. Завершить покупки и пройти на кассу.''')
    try:
        print('Ваш баланс: ', user_money)
        option_select = int(input("Введите опцию: "))
        if option_select not in range(1, 9):
            print("Вы выбрали несуществущюю опцию!")
            options()
        elif option_select == 1:
            all_products()
        elif option_select == 2:
            search_by_name()
        elif option_select == 3:
            add_item()
        elif option_select == 4:
            clear_basket()
        elif option_select == 5:
            show_basket()
        elif option_select == 6:
            del_item()
        elif option_select == 7:
            check_money()
        elif option_select == 8:
            payment()
    except ValueError:
        print('Неверный формат ввода!')
        options()


def check_money():
    print("Ваш баланс составляет: {0} сом".format(user_money))
    options()


def show_basket():
    if purchase_basket == []:
        print("Ваша корзина пуста!")
        options()
    else:
        print("Список товаров в вашей корзине: ")
        for item in purchase_basket:
            print("{} - {} сом".format(item["name"], item["price"]))
        options()


def payment():
    if purchase_basket == []:
        print("Ваша корзина пуста!")
        options()
    else:
        print("Список товаров в вашей корзине: ")
        for item in purchase_basket:
            print("{} - {} сом".format(item["name"], item["price"]))
        purchase_basket.clear()
        print('Спасибо за покупку! Приходите еще!')
        print("Ваша сдача: ", user_money)


def all_products():
    print("Список продуктов и их цена: ")
    for item in products:
        print("{} - {} сом".format(item["name"], item["price"]))
    options()


def search_by_name():
    product = str(input("Введите название товара, чтобы найти его: "))
    name = [x['name'] for x in products]
    if product in name:
        print(product + " имеется в наличий!")
        options()
    else:
        print(denial)
        options()


def add_item():
    print("Список продуктов и их ID: ")
    for item in products:
        print("{} - {}".format(item["name"], item["id"]))
    added_item = int(input('Для добавления товара введите его id: '))
    try:
        for id in products:
            if added_item == id['id']:
                purchase_basket.append(id)
                global user_money
                user_money = user_money - id['price']
                if user_money < 0:
                    user_money = user_money + id['price']
                    purchase_basket.remove(id)
                    print('У вас недостаточно баланса!')
                    options()
                print('''Товар добавлен в корзину!
            Что вы хотите выбрать дальше?
            1. Завершить покупки и пройти на кассу.
            2. Продолжить покупку.
            3. Посмотреть корзину.
            4. Посмотреть баланс.
            5. Вернуться в меню. ''')
        question = int(input())
        if question == 1:
            payment()
        elif question == 2:
            add_item()
        elif question == 3:
            show_basket()
        elif question == 4:
            check_money()
        elif question == 5:
            options()
        else:
            print('Товар с таким ID не существует!')
    except ValueError:
        print('Неверный формат ввода!')
        options()


def clear_basket():
    global user_money
    if purchase_basket == []:
        print("Ваша корзина пуста!")
        options()
    else:
        print("ВНИМАНИЕ! Вы нажали удалить корзину. Если Вы уверены в этом, пожалуйста введите: УДАЛИТЬ")
        affirmative = str(input())
        if affirmative == "УДАЛИТЬ":
            for price in purchase_basket:
                user_money = user_money + price['price']
            purchase_basket.clear()
            print("Ваша корзина очищена!")
            options()
        else:
            print("Продолжаем покупку!")
            options()


def del_item():
    global user_money
    if purchase_basket == []:
        print("Ваша корзина пуста!")
        options()
    else:
        print("Список товаров в Вашей корзине: ")
        for item in purchase_basket:
            print("{} - {}".format(item["name"], item["id"]))
        for del_item in purchase_basket:
            product_delete = int(input('Для удаления товара введите его id: '))
            if del_item['id'] == product_delete:
                user_money = user_money + del_item['price']
                purchase_basket.remove(del_item)
                print('Товар удален!')
                options()
            else:
                print('Товар с таким ID отсутствует в вашей корзине!')
                options()


if __name__ == '__main__':
    main()
