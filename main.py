from task import Task
from datetime import *
from lecture import *
import os

# fonction pour clear la consoel
def cls():
    os.system("cls" if os.name == "nt" else "clear")


def add_task(task):
    liste_task.append(task)
# Main




if __name__ == "__main__":
    cls()
    
    
    #lecture de tout les fichier et stockages dans des listes
    liste_task=read_task_file()
    add_task(Task("la vaiselle","2002-02-12","2002-02-15",7))










### fermeture du programme écriture de tout les données dans les fichiers
    liste_task_dico=[]
    for task in liste_task:
        liste_task_dico.append(task.transform_to_dico())
    print("dico" , liste_task_dico)
    write_file_data('Fichier/test.json', liste_task_dico)

