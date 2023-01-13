import json
from task import *
from reward import *
from task_history import *
from user import *


# lis un fichier json et stock tout dans un liste d'objet data
def read_file_data(filename):
    data = []
    try:
        with open(filename) as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Fichier introuvable.")
    except IOError:
        print("Erreur IO.")
    return data

#écris dans le fichier filename ce qu'il y a dans liste
def write_file_data(filename, liste):
    try:
        with open(filename, "w", encoding="utf-8" ) as file:
            file.write(json.dumps(liste))
            file.close()
    except FileNotFoundError:
        print("Fichier introuvable.")
    except IOError:
        print("Erreur IO.")


################### fonction générique pour écrire dans tout les fichiers ce qu'il faut


def write_liste_data(liste,file):
    liste_data=[]
    for item in liste:
        liste_data.append(item.transform_to_dico())
    write_file_data(file, liste_data)

################### Lecture Task

def read_task_file():
    liste_task=[]
    data_task=read_file_data('fichier/task.json')
    for task in data_task:
        desc=task["desc"]
        last_time=task["last_time"]
        limite_time=task["limite_time"]
        frequency=task["frequency"]
        done=task["done"]
        liste_task.append(Task(desc,last_time,limite_time,frequency,done))
    return liste_task


################### Lecture Reward


def read_reward_file():
    liste_reward=[]
    data_reward=read_file_data('fichier/reward.json')
    for reward in data_reward:
        costpoint=reward["cost_point"]
        name=reward["name"]
        liste_reward.append(Reward(costpoint,name))
    return liste_reward

################### Lecture TaskHistory


def read_task_history_file():
    liste_task_history=[]
    data_task_history=read_file_data('fichier/task_history.json')
    for task_history in data_task_history:
        print("lecture",task_history)
        description_task=task_history["description_task"]
        date_done=task_history["date_done"]
        user_did =task_history["user_did"]
        liste_task_history.append(TaskHistory(description_task,date_done,user_did))
    return liste_task_history


################### Lecture TaskHistory


def read_user_file():
    liste_user=[]
    data_user=read_file_data('fichier/user.json')
    for user in data_user:
        print("lecture",user)
        name=user["name"]
        status=user["status"]
        point =user["point"]
        reward_list =user["reward_list"]
        liste_user.append(User(name,status,point,reward_list))
    return liste_user