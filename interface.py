import os
import time
from parent import Parent

# function to clear console

def cls():
    os.system("cls" if os.name == "nt" else "clear")

# function to handle error in input 


def error_int_input(string,function_callback):
    userinput=input(string)
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
   
    while(True):
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
            while(True):
                userinput=input("Mot De Passe\n")
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

def menu(user,data):
    
    menu_passed=False
    parent= isinstance(user, Parent)

    task="1) les Tâches"
    reward="2) les Récompenses"
    scoreboard="3) le Scoreboard"
    task_history="4) L'historique des Tâches"
    users="5) Liste des Enfants"
    task_to_validated="6) les Tâches à valider"
    reward_to_grand="7) les Récompenses à donner"
    quite="0) Déconnexion"

    while(not menu_passed):
        print("Voici le Menu ?\n")
        print(task)
        print(reward)
        print(scoreboard)
        
        if parent:
            print(task_history)
            print(users)
            print(task_to_validated)
            print(reward_to_grand)
        print(quite)
        menu_passed=True

        userinput=error_int_input("Où veux-tu aller ?",lambda : menu(user,data))

        match userinput:
            case 1:
                menu_passed = True
                cls()
                task_menu(user, data)
            case 2:
                menu_passed = True
                cls()
                reward_menu(user, data)
            case 3:
                menu_passed = True
                cls()
                scoreboard_menu(user,data)
                #
            case 4 if parent:
                menu_passed = True
                cls()
                task_history_menu(user,data)

            case 5 if parent:
                menu_passed = True
                cls()
                children_menu(user, data)

            case 6 if parent:
                menu_passed = True
                cls()
                task_to_validated_menu(user, data)

            case 7 if parent:
                menu_passed = True
                cls()
                reward_to_be_granted_menu(user, data)

            case 0:
                menu_passed = True
                cls()
                close_app(data)
            case _:
                cls()
                print("réponse non valide. \n")

def task_menu(user,data):
    data.show_list_task()
    if isinstance(user, Parent):
        pass
    else:
        pass

def reward_menu(user,data):
    data.show_list_reward()
    if isinstance(user, Parent):
        pass
    else:
        pass

def reward_to_be_granted_menu(user,data):
    data.show_list_reward_to_be_granted()
    

def task_history_menu(user, data):
    while True:
        data.show_list_task_history()
        print("0) Retour au menu principal\n")

        userinput = error_int_input("Sélectionnez une tâche pour afficher son historique (ou 0 pour revenir) : ", lambda: task_history_menu(user, data))

        if userinput == 0:
            cls()
            menu(user, data) 
            return
        else:
            cls()
            print("Choix non valide. Veuillez sélectionner un numéro valide ou 0 pour revenir au menu principal.\n")


def task_to_validated_menu(user, data):
    while True:
        data.show_list_task_to_validated()
        print("(0) Retour au menu principal\n")

        userinput = error_int_input("Sélectionnez une tâche à valider\n ", lambda: task_to_validated_menu(user, data))

        if userinput == 0:
            cls()
            menu(user, data)  # Appel à la fonction menu pour revenir au menu principal
            return
        elif 0 < userinput <= len(data.list_task_to_validated):
            cls()
            # Traitez la tâche à valider sélectionnée ici
        else:
            cls()
            print("Choix non valide. Veuillez sélectionner un numéro valide ou 0 pour revenir au menu principal.\n")
def scoreboard_menu(user,data):
    data.show_list_children()

def children_menu(user,data):
    count=0
    for children in data.list_children:
        count+=1
        print(str(count)+') ' +str(children.name))
        