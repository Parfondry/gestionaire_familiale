import os
import time
from parent import Parent
from task import Task

# function to clear console


def cls():
    os.system("cls" if os.name == "nt" else "clear")

# function to handle error in input


def error_int_input(string, function_callback):
    userinput = input(string)
    if userinput.isdigit():
        return int(userinput)
    else:
        cls()
        print("Erreur : l'entrée doit être un nombre entier\n")
        return function_callback()

# function end


def close_app(data):
    cls()
    print("Au revoir !")
    time.sleep(1)
    data.write_data()

# connection screen


def connection(data):

    while (True):
        print("Bienvenue dans le gestionaire de taches familiales.")
        print("")

        count = 0
        print("(-1) Parent")
        for child in data.list_children:
            count += 1
            print("(" + str(count) + ") " + child.name)
        print("")
        print("(0) quitter\n")

        userinput = input("Qui est-tu ?\n")

        if userinput.isdigit():
            userinput = int(userinput)
            if 0 < userinput <= len(data.list_children):
                return data.list_children[userinput - 1]
            elif userinput == 0:
                cls()
                connection(data)
                return None
        elif userinput == "-1":
            cls()
            while (True):
                userinput = input("Mot De Passe\n")
                if userinput == "Admin":
                    cls()
                    return Parent("Admin", "Admin")
        cls()
        print("Veuillez entrer un chiffre valide.\n")


def connexion_parent(data):
    while True:
        print("Bonjour !\n")
        print("Veuillez entrer le mot de passe\n")
        print("(0) retour\n")
        userinput = input("Mot de passe ?\n")

        if userinput == "Admin":
            cls()
            return Parent("Admin", "Admin")
        elif userinput == "0":
            cls()
            connection(data)

        else:
            cls()
            print("Mot de passe non valide. \n")


# main menu enfant

def menu(user, data):

    menu_passed = False
    parent = isinstance(user, Parent)

    task = "1) les Tâches"
    reward = "2) les Récompenses"
    scoreboard = "3) le Scoreboard"
    task_history = "4) L'historique des Tâches"
    users = "5) Liste des Enfants"
    task_to_be_validated = "6) les Tâches à valider"
    reward_to_grand = "7) les Récompenses à donner"
    quite = "0) Déconnexion"

    while (not menu_passed):
        print("Voici le Menu ?\n")
        print(task)
        print(reward)
        print(scoreboard)

        if parent:
            print(task_history)
            print(users)
            print(task_to_be_validated)
            print(reward_to_grand)
        print(quite)

        userinput = input("Où veux-tu aller ?")
        if userinput.isdigit():
            userinput = int(userinput)
            match userinput:
                case 1:
                    cls()
                    if isinstance(user, Parent):
                        task_menu_parent(user, data)
                    else:
                        task_menu_enfant(user, data)
                case 2:

                    cls()
                    if isinstance(user, Parent):
                        reward_menu_parent(user, data)
                    else:
                        reward_menu_enfant(user, data)
                case 3:

                    cls()
                    scoreboard_menu(user, data)
                    #
                case 4 if parent:

                    cls()
                    task_history_menu(user, data)

                case 5 if parent:

                    cls()
                    # children_menu(user, data)

                case 6 if parent:

                    cls()
                    task_to_be_validated_menu(user, data)

                case 7 if parent:

                    cls()
                    reward_to_be_granted_menu(user, data)

                case 0:
                    menu_passed = True
                    cls()
                    close_app(data)
                case _:
                    cls()
                    print("réponse non valide. \n")
        else:
            cls()
            print("réponse non valide. \n")

# Fait


def task_menu_parent(user, data):
    flag = True
    while flag:
        print("La Liste des Tâches\n")
        data.show_list_task()
        print("\nLes commandes : \n")
        print("Pour modifier une tâche veuillez insérer son numéro. ")
        print("Pour ajouter une tâche insérez : -1")
        print("Pour Retourner au menu principal insérez 0\n")
        userinput = input("Insérez valeur : ")
        if userinput.isdigit():
            userinput = int(userinput)
            if userinput == 0:
                cls()
                flag = False
            elif 0 < userinput <= len(data.list_task):
                cls()
                task = data.list_task[userinput-1]
                print("Vous modifier la Tâche :", task.description)
                print("Voulez vous la supprimer ?")
                supprimer = input(
                    "Si oui appuyer sur 0, si non appuyer sur n'importe quel autre touche : ")
                if supprimer == "0":
                    data.del_task(userinput-1)
                    cls()
                    print("La tâche a bien été supprimée")
                    input("Veuillez appuyer sur une touche pour continuer.")
                else:
                    point = ""
                    limite_time = ""
                    description = input(
                        "Veuillez insérer la description de la tâche : ")
                    flag_limite_time = True
                    while flag_limite_time:
                        limite_time = input(
                            "Veuillez insérer la date limite de votre tâche (format : AAAA-MM-JJ) : ")
                        date_components = limite_time.split('-')

                        if len(date_components) == 3:
                            year, month, day = date_components

                            if year.isdigit() and month.isdigit() and day.isdigit():
                                if len(year) == 4 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                                    flag_limite_time = False
                                else:
                                    print(
                                        "Format de date incorrect. Veuillez utiliser le format AAAA-MM-JJ avec des valeurs valides.")
                            else:
                                print(
                                    "Format de date incorrect. Veuillez utiliser des chiffres pour les composants de la date.")
                        else:
                            print(
                                "Format de date incorrect. Veuillez utiliser le format AAAA-MM-JJ.")

                    flag_point = True
                    while flag_point:
                        point = input(
                            "Veuillez insérer le nombre de points de votre Tâche : ")
                        if point.isdigit():
                            point = int(point)
                            flag_point = False
                        else:
                            print("Veuillez entrer un nombre entier valide.")
                    cls()
                    print(description, "a bien été ajoutée à la liste des tâches")
                    data.update_task(userinput, Task(
                        description, "2100-1-1", limite_time, point))
                    input("appuyer sur n'importe quel touche pour continuer")
                    cls()

        elif userinput == "-1":
            cls()
            point = ""
            limite_time = ""
            description = input(
                "Veuillez insérer la description de la tâche : ")
            flag_limite_time = True
            while flag_limite_time:
                limite_time = input(
                    "Veuillez insérer la date limite de votre tâche (format : AAAA-MM-JJ) : ")
                date_components = limite_time.split('-')

                if len(date_components) == 3:
                    year, month, day = date_components

                    if year.isdigit() and month.isdigit() and day.isdigit():
                        if len(year) == 4 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                            flag_limite_time = False
                        else:
                            print(
                                "Format de date incorrect. Veuillez utiliser le format AAAA-MM-JJ avec des valeurs valides.")
                    else:
                        print(
                            "Format de date incorrect. Veuillez utiliser des chiffres pour les composants de la date.")
                else:
                    print(
                        "Format de date incorrect. Veuillez utiliser le format AAAA-MM-JJ.")

            flag_point = True
            while flag_point:
                point = input(
                    "Veuillez insérer le nombre de points de votre Tâche : ")
                if point.isdigit():
                    point = int(point)
                    flag_point = False
                else:
                    print("Veuillez entrer un nombre entier valide.")
            print(description, "a bien été ajoutée à la liste des tâches")
            data.add_task(Task(description, "2100-1-1", limite_time, point))
            input("appuyer sur n'importe quel touche pour continuer")
            cls()

        else:
            cls()
            print("Choix non valide. Veuillez sélectionner un numéro valide ou 0 pour revenir au menu principal.\n")

# Fait


def task_menu_enfant(user, data):
    flag = True
    while flag:
        print("La Liste des Tâches\n")
        data.show_list_task()
        print("0) Pour revenir au menu")
        userinput = input(
            "\n Met le numéro de la tâche que tu souhaites effecuter : ")
        if userinput.isdigit():
            userinput = int(userinput)
            if userinput == 0:
                flag = False
                cls()
            elif 0 < userinput <= len(data.list_task):
                cls()
                selected_task = data.list_task[userinput - 1]
                user.request_task(selected_task, data)
                input(
                    "La tâche est en attente de validation, appuies sur n'importe quel bouton pour continuer : ")
            else:
                cls()
                print(
                    "Choix non valide. Veuillez sélectionner un numéro valide ou 0 pour revenir au menu principal.\n")
        else:
            cls()
            print("Veuillez entrer un numéro valide.\n")


def reward_menu_parent(user, data):
    data.show_list_reward()

# Fait


def reward_menu_enfant(user, data):
    flag = True
    while flag:
        print("La Liste des Récompenses\n")
        data.show_list_reward()
        print("0) Pour revenir au menu")
        userinput = input('Choissisez une récompense : ')
        if userinput.isdigit():
            userinput = int(userinput)
            if userinput == 0:
                flag = False
                cls()
            elif 0 < userinput <= len(data.list_reward):
                cls()
                print('o')
                selected_reward = data.list_reward[userinput - 1]
                print(selected_reward)
                if selected_reward.cost <= user.point:
                    user.request_reward(selected_reward, data)
                    user.point = user.point-selected_reward.cost
                    input(
                        "La récompense est en attente de validation, appuies sur n'importe quel bouton pour continuer : ")
                    cls()
                else:
                    print("Vous n'avez pas assez de points.\n")
            else:
                cls()
                print(
                    "Choix non valide. Veuillez sélectionner un numéro valide ou 0 pour revenir au menu principal.\n")
        else:
            cls()
            print("Veuillez entrer un numéro valide.\n")

    input()


def reward_menu_parent(user, data):
    pass


def reward_to_be_granted_menu(user, data):
    data.show_list_reward_to_be_granted()


# Fait
def task_history_menu(user, data):
    flag = True
    while flag:
        data.show_list_task_history()

        userinput = input("\n0) Retour au menu principal\n ")

        if userinput == '0':
            cls()
            flag = False
        else:
            cls()
            print("Choix non valide. Veuillez sélectionner un numéro valide ou 0 pour revenir au menu principal.\n")

# FAIT


def task_to_be_validated_menu(user, data):
    flag = True
    while flag:
        data.show_list_task_to_be_validated()
        print("(0) Retour au menu principal\n")
        userinput = input(
            "Sélectionnez une tâche à valider\n Pour passer en mode refuser mettez un -\n")
        if userinput.isdigit():
            userinput = int(userinput)
            if userinput == 0:
                cls()
                flag = False
            elif 0 < userinput <= len(data.list_task_to_be_validated):
                task_history = data.list_task_to_be_validated[userinput-1]
                child = data.find_children(task_history.children)
                user.accept_task(task_history, child, data)
                cls()
                print(
                    "La Tâche a bien été validée, Selectionnez une autre Tâche à valider\n")
        elif userinput == "-":
            userinput = input("Sélectionnez une tâche à supprimer\n")
            if userinput.isdigit():
                userinput = int(userinput)
                if userinput == 0:
                    cls()
                    flag = False
                elif 0 < userinput <= len(data.list_task_to_be_validated):
                    task_history = data.list_task_to_be_validated[userinput-1]
                    user.reject_task(task_history, data)
                    cls()
                    print(
                        "La Tâche a bien été supprimér, Appuyer sur une touche pour continuer\n")

        else:
            cls()
            print("Choix non valide. Veuillez sélectionner un numéro valide ou 0 pour revenir au menu principal.\n")
    menu(user, data)


def scoreboard_menu(user, data):
    data.show_list_children()
