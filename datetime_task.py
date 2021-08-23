# 1. Написать программу с помощью которой пользователь, по выбору, может посмотреть
# - текущее число
# - месяц
# - год
# - время
# - полную дату и время в формате '%m/%d/%Y %H:%M:%S'

import datetime
import time

print('Добро пожаловать в программу "Время"!')
while True:
    try:
        user_option = int(input('''Выберите, что Вы хотите посмотреть:
                           1 - Текущее число
                           2 - Месяц
                           3 - Год
                           4 - Время
                           5 - Полную дату и время в формате m/d/Y h:m:s (08/21/2021 12:36:12)
                           Ваш ввод:'''))
        if user_option == 1:
            print(datetime.datetime.now().day)
        elif user_option == 2:
            print(datetime.datetime.now().month)
        elif user_option == 3:
            print(datetime.datetime.now().year)
        elif user_option == 4:
            print(datetime.datetime.now().strftime('%H:%M:%S'))
        elif user_option == 5:
            print(datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
        else:
            print('Введите цифру правильно!')
    except ValueError:
        print("Неверный формат ввода!")

