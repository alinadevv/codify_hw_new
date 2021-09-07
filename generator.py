class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class TablePrinter:
    def desribe_users(self, users):
        pass


user_1 = User('Alina', 'asdf@mail.ru', 'qwerty')
user_2 = User('Nikita', 'qwerty@mail.ru', 'asdf')
user_3 = User('Nigora', 'zxcv@mail.ru', 'ghjkj')

users_group = ([user_1, user_2, user_3])

for user_group in users_group:
    print(user_group.username, user_group.email, user_group.password)