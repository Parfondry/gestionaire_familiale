from datetime import *
import os
from task import *
from reward import *
from task_history import *
from user import *
from children import Children
from datamanager import DataManager
from interface import *


if __name__ == "__main__":
    cls()
    data = DataManager()
    data.load_data()
    user=connection(data)
    print(user.name)
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
