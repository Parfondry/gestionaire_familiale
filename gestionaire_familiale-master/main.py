# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from task import Task
import os

# fonction pour clear la consoel
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

liste = [Task(1,"faire le ménage"),Task(2,"faire la vaisselle"),Task(3,"Sortir la poubelle")]

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cls()
    for i in liste:
        i.str()
    a=1
    while a!=0:
        a=int(input("Insérer un numéro afin de modifier l'état de la tache correspondante, et insérez 0 pour fermer \n"))
        if a!=0 and a>0 and a<len(liste):
            liste[a-1].set_done(True)
            input("Veuillez insérer n'importe quelle touche pour réafficher la liste \n")
            cls()
            for i in liste:
              i.str()
        elif a!=0:
            print("veuillez insérer un nombre valide")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
