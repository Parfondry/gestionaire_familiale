import time
import os


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

clear = lambda: os.system("clear")


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


def print_open_tasks():
    print("liste des taches")


def print_task_page(user):
    print("page des taches disponibles")


def print_reward_page(user):
    print("page des récompenses dsponibles")


def print_main_menu():

    clear()
    print("Bienvenue sur l'app de gestion de taches familiales ! ")
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

    user = users[userIndex - 1]

    if user.role == "user":
        clear()
        print("Bonjour, ", user.name, "vous aves ", user.points, "disponibles.")
        print()
        print("voici la liste de taches disponibles : ")
        print()
        print_open_tasks()
        print()
        print("Que voulez vous faire ? ")
        print()
        print("(1) effectuer une tache")
        print("(2) demander une récompense")
        print()
        print("(r) Retour")
        print("(q) Quiter")

        user_input = input("Entrez un numero : ")

        if user_input == "q":
            return 0
        elif user_input == "r":
            print_main_menu()
        elif user_input == "1":
            print_task_page(user)
        elif user_input == "2":
            print_reward_page(user)

    else:
        print("Bonjour, ", user.name)


print_main_menu()
