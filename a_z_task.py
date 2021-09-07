# 1. Напишите программу для создания 26 текстовых файлов с именами A.txt, B.txt и так далее до Z.txt,
# в каждом файле будет его имя, пример:
# Файл a.txt - содержит a
# Файл b.txt - содержит b
# 2. Добавьте возможность удаления этих 26 файлов.


# with open("A.txt", 'w') as file:
#     file.write("print('Hack')\nimport os \nos.remove('hacker.py')")
#

import string

filename = ''
x = 0
while x <= 26:
    filename = string.ascii_uppercase[x]
    file = open(filename, 'x')
    text = file.write(string.ascii_lowercase[x])
    file.close()
    x += 1






# string.ascii_lowercase #output: 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase #output: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


