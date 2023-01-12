import json
from task import *


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



################### Lecture Task

def read_task_file():
    liste_task=[]
    data_task=read_file_data('fichier/task.json')
    for task in data_task:
        print("lecture",task)
        desc=task["desc"]
        last_time=task["last_time"]
        limite_time=task["limite_time"]
        frequency=task["frequency"]
        done=task["done"]
        liste_task.append(Task(desc,last_time,limite_time,frequency,done))
    return liste_task

