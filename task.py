from datetime import datetime
from task_history import TaskHistory

class Task:
    current_id=0

    #l'id s'incrémente à chaque nouvel instance créer de telle manière que chaque instance a un id unique
    def __init__(self, desc,last_time,limite_time,point):
        date_format = "%Y-%m-%d"
        self.__desc =desc
        self.__point = point
        self.__last_time = datetime.strptime(last_time, date_format).date()
        self.__limite_time = datetime.strptime(limite_time, date_format).date()

    @property
    def desc(self):
        return self.__desc

    @property
    def point(self):
        return self.__point


    @property
    def last_time(self):
        return self.__last_time

    @property
    def limite_time(self):
        return self.__limite_time



    @last_time.setter
    def last_time(self,new_last_time):
        self.__last_time=new_last_time

    @limite_time.setter
    def limite_time(self,new_limite_time):
        self.__limite_time=new_limite_time

    @point.setter
    def point(self,new_point):
        self.__frequency=new_point

    @desc.setter
    def desc(self,new_desc):
        self.__desc=new_desc


    ### input self, et un children
    ### output une task history

    def task_done(self,children):
        date_format = "%Y-%m-%d"
        time_now = datetime.now()
        time_now = time_now.strftime(date_format)
        return TaskHistory(self.desc,time_now,children.name)
               


    #fonction qui permet de transformer un objet TASK en un dictionaire.
    def transform_to_dico(self):
        dico={'desc':self.desc,'last_time':self.last_time.strftime("%Y-%m-%d"),'limite_time':self.limite_time.strftime("%Y-%m-%d"),'point':self.point}
        return dico

    def __repr__(self):
        return(' desc : ' + str(self.desc))