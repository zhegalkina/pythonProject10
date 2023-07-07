class User:
    def __init__(self, login, password, status):
        self.login = login
        self.password = password
        self.status = status

users = []

user_1 = User("ttt", 5555, "user")
users.append(user_1)

user_2 = User("uuu", 888, "user")
users.append(user_2)

