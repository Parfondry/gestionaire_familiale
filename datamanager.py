
from file_read_write import *

class DataManager():

    
    def __init__(self, list_task=[], list_reward=[], list_task_history=[], list_reward_to_be_granted=[], list_task_to_be_validated=[], list_children=[]):
        
        self.__list_task=list_task
        self.__list_reward=list_reward
        self.__list_task_history=list_task_history
        self.__list_reward_to_be_granted=list_reward_to_be_granted
        self.__list_task_to_be_validated=list_task_to_be_validated
        self.__list_children=list_children


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
    def list_task_to_validated(self):
        return self.__list_task_to_be_validated
    
    @property
    def list_children(self):
        return self.__list_children
    
    @list_children.setter
    def list_children(self,new_value):
        self.__list_children=new_value

    @list_reward.setter
    def list_reward(self,new_value):
        self.__list_reward=new_value

    @list_reward_to_be_granted.setter
    def list_reward_to_be_granted(self,new_value):
        self.__list_reward_to_be_granted=new_value

    @list_task_history.setter
    def list_task_history(self,new_value):
        self.__list_task_history=new_value

    @list_task.setter
    def list_task(self,new_value):
        self.__list_task=new_value

    @list_task_to_validated.setter
    def list_task_to_validated(self,new_value):
        self.__list_task_to_be_validated=new_value

    def load_data(self):
        self.list_task=read_task_file()
        self.list_children=read_children_file()
        self.list_reward = read_reward_file()
        self.list_reward_to_be_granted = read_reward_to_be_granted_file()
        self.list_task_history = read_task_history_file()
        self.list_task_to_validated = read_task_to_be_validated()

    def write_data(self):
        write_list_data(self.list_task,'fichier/task.json')
        write_list_data(self.list_children,'fichier/children.json')
        write_list_data(self.list_reward,'fichier/reward.json')
        write_list_data(self.list_task_to_validated,'fichier/task_to_validated.json')
        write_list_data(self.list_task_history,'fichier/task_history.json')
        write_list_task_to_be_validated(self.list_reward_to_be_granted,'fichier/reward_to_be_granted.json')