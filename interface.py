import os
import time


# function to clear console

def cls():
    os.system("cls" if os.name == "nt" else "clear")


# main menu enfant

def main_enfant():
    cls()
    print("main_enfant")


def conn_enfant(data):
    cls()
    print("Bonjour !")
    print("")

    count = 0
    for child in data.list_children:
        count += 1
        print("(" + str(count) + ") " + child.name)

    print("")
    print("(0) retour")
    userinput = int(input("Qui est tu ?"))

    if userinput == 0:
        connection(data)

    main_enfant(data)


def pass_parent(data):
    print("pass_parent")


# connection screen

def connection(data):
    cls()
    print("Bienvenue dans le gestionaire de taches familiales.")
    print("")
    print("(1) Un enfant ")
    print("(2) un parrent ")
    print("")
    print("(0) quitter ")

    userinput = int(input("Qui etes vous ?"))

    match userinput:
        case 1:
            conn_enfant(data)
        case 2:
            pass_parent(data)
        case _:
            print("réponse non valide")
            time.sleep(2)
            connection(data)
