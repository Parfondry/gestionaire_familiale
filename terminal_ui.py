import time


class User:
    def __init__(self, name, role, points):
        self.name = name
        self.role = role
        self.points = points


users = [
    User("Alice", "user", 200),
    User("Daniel", "user", 300),
    User("Marie", "user", 100),
    User("Fabrice", "admin", 0),
    User("Jeanne", "admin", 0),
]


def print_scroeboard():

    print("Scoreboard :")
    print()

    copy_users = users.copy()

    copy_users.sort(key=lambda copy_users: copy_users.points, reverse=True)

    compteur = 1

    for i in copy_users:
        if i.points >> 0:
            print("numero", compteur, ":", i.name, "avec", i.points, "points !")
            compteur += 1


def print_main_menu():

    print()
    print("Bienvenue sur l'app de gestin de taches familiales ! ")
    print()
    print_scroeboard()
    print()
    print("Qui etes vous ?")
    print()
    compteur = 1

    for i in users:
        print("(", compteur, ")", i.name)
        compteur += 1

    print()
    print("( q ) Quiter")
    print()

    user_input = input("Entrez un numero : ")

    if user_input == "q":
        return 0
    else:
        print_user_page(int(user_input))


def print_user_page(userIndex):

    user = users[userIndex]

    if user.role == "user":
        print("user")
    else:
        print("admin")


print_main_menu()
