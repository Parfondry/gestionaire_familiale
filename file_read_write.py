
import json
from task import Task
from reward import Reward
from task_history import TaskHistory
from children import Children

# open and read a json file
# input the name of the file as filename
# outpute a list data with all the data
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

# write data in json in a file
# input the data (liste) and the file (filename)
# output : nothing
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

# function who gets a liste of a type of object and a filename to put the file
# the function transform with the methode transfor_to_dico objects into dico
# output: nothing
def write_list_data(list,filename):
    list_data=[]
    for item in list:
        list_data.append(item.transform_to_dico())
    write_file_data(filename, list_data)

###### fonction pour écrire la reward to be granted
def write_list_reward_to_be_granted(list,filename):
    list_data=[]
    for item in list:
        reward_to_be_granted_dict=item[0].transform_to_dico()
        reward_to_be_granted_dict['user']=item[1]
        list_data.append(reward_to_be_granted_dict)
    write_file_data(filename, list_data)


################### Lecture Task

def read_task_file():
    liste_task=[]
    data_task=read_file_data('fichier/task.json')
    for task in data_task:
        description=task["description"]
        last_time=task["last_time"]
        limite_time=task["limite_time"]
        point=task["point"]
        liste_task.append(Task(description,last_time,limite_time,point))
    return liste_task


################### Lecture Reward


def read_reward_file():
    liste_reward=[]
    data_reward=read_file_data('fichier/reward.json')
    for reward in data_reward:
        name=reward["name"]
        cost=reward["cost"]        
        liste_reward.append(Reward(name,cost))
    return liste_reward

################### Lecture TaskHistory


def read_task_history_file():
    liste_task_history=[]
    data_task_history=read_file_data('fichier/task_history.json')
    for task_history in data_task_history:
        description_task=task_history["description_task"]
        date_done=task_history["date_done"]
        children =task_history["children"]
        point=task_history["point"]
        liste_task_history.append(TaskHistory(description_task,date_done,children,point))
    return liste_task_history


################### Lecture TaskHistory


def read_children_file():
    liste_children=[]
    data_children=read_file_data('fichier/children.json')
    for children in data_children:
        name=children["name"]
        point =children["point"]
        reward_list =children["reward_list"]
        liste_children.append(Children(name,point,reward_list))
    return liste_children


################### Lecture Reward to be granted


def read_reward_to_be_granted_file():
    liste_reward_to_be_granted=[]
    data_reward_to_be_granted=read_file_data('fichier/reward_to_be_granted.json')
    for reward_and_name in data_reward_to_be_granted:
        name=reward_and_name["name"]
        cost=reward_and_name["cost"]
        user=reward_and_name["user"]        
        liste_reward_to_be_granted.append([Reward(name,cost),user])
    return liste_reward_to_be_granted


################### Lecture Task ro be validated


def read_task_to_be_validated():
    liste_task_to_be_validated=[]
    data_task_to_be_validated=read_file_data('fichier/task_to_be_validated.json')
    for task_to_be_validated in data_task_to_be_validated:
        description_task=task_to_be_validated["description_task"]
        date_done=task_to_be_validated["date_done"]
        children =task_to_be_validated["children"]
        point=task_to_be_validated['point']
        liste_task_to_be_validated.append(TaskHistory(description_task,date_done,children,point))
    return liste_task_to_be_validated