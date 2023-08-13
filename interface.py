import os
import time

# function to clear console

def cls():
    os.system("cls" if os.name == "nt" else "clear")

# function to handle error in input 


def error_int_input(string,function_callback):
    try:
        userinput = int(input(string)) 
        return userinput
    except ValueError:
        cls()
        print("Erreur : l'entrée doit être un nombre entier\n")
        function_callback()

# function end 
def close_app(data):
    cls()
    print("Au revoir !")
    time.sleep(3)
    data.write_data()

# connection screen

def connection(data):

    connexion_passed=False
    
    while(not connexion_passed):
        print("Bienvenue dans le gestionaire de taches familiales.")
        print("")
        print("(1) Un enfant ")
        print("(2) un parent ")
        print("")
        print("(0) quitter ")
    
    
        userinput=error_int_input("Qui êtes vous ?\n",lambda : connection(data))

        match userinput:
            case 1:
                connexion_passed=True
                return(connexion_enfant(data))
            case 2:
                connexion_passed=True
                pass_parent(data)
            case 0:
                connexion_passed=True
                close_app(data)
            case _:
                cls()
                print("réponse non valide. \n")
            



def connexion_enfant(data):
    cls()
    print("Bonjour !")
    print("")

    count = 0
    for child in data.list_children:
        count += 1
        print("(" + str(count) + ") " + child.name)

    print("")
    print("(0) retour")
    userinput = error_int_input("Qui est-tu ?",lambda :connexion_enfant(data))
    return(data.list_children[userinput-1])




def pass_parent(data):
    print("pass_parent")

 
# main menu enfant

def main_enfant(data):
    cls()
    print("main_enfant")
