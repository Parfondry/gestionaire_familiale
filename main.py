from task import *
from reward import *
from task_history import *
from user import *
from datetime import *
from lecture import *
import os

# fonction pour clear la consoel


def cls():
    os.system("cls" if os.name == "nt" else "clear")


# def add_task(task):
#     liste_task.append(task)
# def add_reward(reward):
#     liste_reward.append(reward)
# def add_task_history(task_history):
#     liste_task_history.append(task_history)
# def add_user(user):
#     liste_user.append(user)
# # Main


if __name__ == "__main__":
    cls()
    print("coucou")

#     #charger les données
#     liste_task=read_task_file()
#     liste_reward=read_reward_file()
#     liste_task_history=read_task_history_file()
#     liste_user=read_user_file()

#     #lecture de tout les fichier et stockages dans des listes


# ### fermeture du programme écriture de tout les données dans les fichiers

#     write_liste_data(liste_task,'Fichier/test.json')
#     write_liste_data(liste_reward,'Fichier/test.json')
#     write_liste_data(liste_task_history,'Fichier/test.json')
#     write_liste_data(liste_user,'Fichier/test.json')
