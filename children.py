from user import User
from datamanager import DataManager
from task import Task


class Children(User):
    def __init__(self, name, type, point, reward_list):
        super().__init__(name, type)
        self.__point = point
        self.__reward_list = reward_list

    @property
    def reward_list(self):
        return self.__reward_list

    @reward_list.setter
    def reward_list(self, new_reward_list):
        self.__reward_list = new_reward_list

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, new_point):
        self.__point = new_point


    #fonction qui prend une tache et qui prends la data en entre
    #elle permet d'ajouter a la liste des taches a verifier la tache effectué
    def request_task(self, task, data):
        task_formated=task.task_to_task_history(self)
        data.add_task_to_be_validated(task_formated)
        

    def transform_to_dico(self):
        dico={'name':self.name,'point':self.point,'reward_list':self.reward_list}
        return dico

