
from file_read_write import *


class DataManager():

    def __init__(self, list_task=[], list_reward=[], list_task_history=[], list_reward_to_be_granted=[], list_task_to_be_validated=[], list_children=[]):

        self.__list_task = list_task
        self.__list_reward = list_reward
        self.__list_task_history = list_task_history
        self.__list_reward_to_be_granted = list_reward_to_be_granted
        self.__list_task_to_be_validated = list_task_to_be_validated
        self.__list_children = list_children

    @property
    def list_task(self):
        return self.__list_task

    @property
    def list_reward(self):
        return self.__list_reward

    @property
    def list_reward_to_be_granted(self):
        return self.__list_reward_to_be_granted

    @property
    def list_task_history(self):
        return self.__list_task_history

    @property
    def list_task_to_be_validated(self):
        return self.__list_task_to_be_validated

    @property
    def list_children(self):
        return self.__list_children

    @list_children.setter
    def list_children(self, new_value):
        self.__list_children = new_value

    @list_reward.setter
    def list_reward(self, new_value):
        self.__list_reward = new_value

    @list_reward_to_be_granted.setter
    def list_reward_to_be_granted(self, new_value):
        self.__list_reward_to_be_granted = new_value

    @list_task_history.setter
    def list_task_history(self, new_value):
        self.__list_task_history = new_value

    @list_task.setter
    def list_task(self, new_value):
        self.__list_task = new_value

    @list_task_to_be_validated.setter
    def list_task_to_be_validated(self, new_value):
        self.__list_task_to_be_validated = new_value

    # méthode permettant l'ajout et la suppression

    # prend un objet Task et l'ajoute a liste des taches
    # input : task => est un objet TASK !!
    def add_task(self, task):
        self.list_task.append(task)

    def add_reward(self, reward):
        self.list_reward.append(reward)

    def add_task_history(self, task_history):
        self.list_task_history.append(task_history)

    def add_task_to_be_validated(self, task_history):
        self.list_task_to_be_validated.append(task_history)

    def add_children(self, children):
        self.list_children.append(children)

    # ici input reward + nom de l'enfant
    def add_reward_to_be_granted(self, reward, children_name):
        self.list_reward_to_be_granted.append([reward, children_name])

    # delete

    def del_task(self, index):
        index=index-1
        if 0 <= index < len(self.list_task):
            del self.list_task[index]
    
    def del_reward(self, index):
        index=index-1
        if 0 <= index < len(self.list_reward):
            del self.list_reward[index]

    def del_task_history(self, index):
        index=index-1
        if 0 <= index < len(self.list_task_history):
            del self.list_task_history[index]

    def del_task_to_be_validated(self, index):
        index=index-1
        if 0 <= index < len(self.list_task_to_be_validated):
            del self.list_task_to_be_validated[index]

    def del_children(self, index):
        index=index-1
        if 0 <= index < len(self.list_children):
            del self.list_children[index]

    def del_reward_to_be_granted(self, index):
        index=index-1
        if 0 <= index < len(self.list_reward_to_be_granted):
            del self.list_reward_to_be_granted[index]

    # update

    def update_task(self, index, new_task):
        index=index-1
        if 0 <= index < len(self.list_task):
            self.list_task[index] = new_task

    def update_reward(self, index, new_reward):
        index=index-1
        if 0 <= index < len(self.list_reward):
            self.list_reward[index] = new_reward

    # inutile normalement
    def update_task_history(self, index, new_task_history):
        index=index-1
        if 0 <= index < len(self.list_task_history):
            self.list_task_history[index] = new_task_history

    def update_children(self, index, new_children):
        index=index-1
        if 0 <= index < len(self.list_children):
            self.list_children[index] = new_children

    # Inutile noramlement

    def update_reward_to_be_granted(self, index, new_reward_data):
        index=index-1
        if 0 <= index < len(self.list_reward_to_be_granted):
            self.list_reward_to_be_granted[index] = new_reward_data


    #find children object
    #cas spécial a traiter..
    def find_children(self,child_name):
        for child in self.list_children:
            if child.name ==child_name:
                return child
            

    ###### Commande de show
    def show_list_task(self):
        count=0
        for task in self.list_task:
            count+=1
            print(str(count) + ")" +str(task))
    
    def show_list_reward(self):
        count = 0
        for reward in self.list_reward:
            count += 1
            print(str(count) + ") " +str(reward))

    def show_list_reward_to_be_granted(self):
        count = 0
        for reward_data in self.list_reward_to_be_granted:
            count += 1
            reward, children_name = reward_data
            print(str(count) + ") " +str(reward.name) + ' pour ' + str(children_name))

    def show_list_task_history(self):
        count = 0
        for task_history in self.list_task_history:
            count += 1
            print(str(count) + ") " +str(task_history))

    def show_list_task_to_be_validated(self):
        count = 0
        for task_history in self.list_task_to_be_validated:
            count += 1
            print(str(count) + ") " +str(task_history))

    def show_list_children(self):
        count = 0
        for child in self.list_children:
            count += 1
            print(str(count) + ") " +str(child))
    #####

    def load_data(self):
        self.list_task = read_task_file()
        self.list_children = read_children_file()
        self.list_reward = read_reward_file()
        self.list_reward_to_be_granted = read_reward_to_be_granted_file()
        self.list_task_history = read_task_history_file()
        self.list_task_to_be_validated = read_task_to_be_validated()

    def write_data(self):
        write_list_data(self.list_task,'fichier/task.json')
        write_list_data(self.list_children,'fichier/children.json')
        write_list_data(self.list_reward,'fichier/reward.json')
        write_list_data(self.list_task_to_be_validated,'fichier/task_to_be_validated.json')
        write_list_data(self.list_task_history,'fichier/task_history.json')
        write_list_reward_to_be_granted(self.list_reward_to_be_granted,'fichier/reward_to_be_granted.json')
        write_list_data(self.list_task, 'fichier/task.json')
  