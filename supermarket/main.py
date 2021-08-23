from meat_milk import main as meat_milk_main
from bakery import main as bakery_main
from fruits import main as fruits_main



def main():
  print("Добро пожаловать в супермаркет!")
  while True:
    try:
      option = int(input('''Выберите одну из опций:
                        1. Перейти в раздел
                        2. Выйти из супермаркета
                        Ваш ввод: '''))
      if option == 1:
        print('''Разделы супермаркета:
                  1. Мясо и молочная продукция
                  2. Выпечка и сладости
                  3. Овощи и фрукты''')
        try:
          supermarket = int(input("Выберите раздел супермаркета, чтобы перейти к продукции: "))
          if supermarket == 1:
            meat_milk_main()
          elif supermarket == 2:
            bakery_main()
          elif supermarket == 3:
            fruits_main()
          else:
            print("Ошибка! Введите цифру правильно!")
        except ValueError:
          print("Ошибка, Вы ввели не число!")
      elif option == 2:
        print("Вы выходите из супермаркета!")
        break
      else:
        print("Ошибка, введите правильное число!")
    except ValueError:
      print("Ошибка, Вы ввели не число!")

main()


if __name__ == '__main__':
  main()




