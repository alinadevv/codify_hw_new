# 1. Напишите программу которая спрашивает ФИО, телефон пользователя и

# записывает их в файл, в виде словаря, обработайте возможные ошибки.

# 2. Расширьте возможность программы (1) добавив поиск по ФИО, телефону.

# 3. Расширьте возможность программы (1) и (2) добавив удаление данных по ФИО, телефону.

user_name = input('Введите Ваше имя: ')
user_tel = input('Введите Ваш телефон: ')

import csv
import os
import sys

FILE_NAME = os.path.join(sys.path[0], 'my_file_new.txt')

my_database = [
    {'name': user_name, 'tel': user_tel}
]

with open(FILE_NAME, 'w') as file:
    writer = csv.DictWriter(file, ['name', 'tel'])
    writer.writeheader()
    writer.writerows(my_database)

with open(FILE_NAME, 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)

user_choice = int(input('''Выберите, что Вы хотите сделать:
1. Поиск по имени
2. Поиск по номеру телефона
Ваш ввод:  '''))
if user_choice == 1:
  find_name = input('Введите имя: ')
  name_to_find = find_name
  print('имя',name_to_find)
elif user_choice == 2:
  find_tel = input('Введите телефон: ')
  tel_to_find = find_tel
  print('номер телефона',tel_to_find)
else:
  print('Неверный ввод!')
