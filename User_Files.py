# Напишите программу которая позволяет пользователю:
# 1. Записать какой-то текст в файл
# 2. Найти записанный текст в файле по дате, либо по содержимому в ней.

import os
import sys
import datetime

FILE_NAME = os.path.join(sys.path[0], 'my_file_new.txt')

user_input = input('Введите текст: ')
with open(FILE_NAME, 'w') as my_file:
    my_time = datetime.datetime.now()
    my_file.write(my_time + "" + user_input)
    my_file.write('my_text \n text 123123123 \n third line')

word_to_find = 'second'
with open(FILE_NAME, 'w') as my_file:
    for line in my_file:
        if word_to_find in line:
            print('Строка найдена', line)

date_day = int(input('Введите число: '))










