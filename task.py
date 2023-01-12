from datetime import *

class Task:
    current_id=0

    #l'id s'incrémente à chaque nouvel instance créer de telle manière que chaque instance a un id unique
    def __init__(self, desc,last_time,limite_time,frequency,done=False):
        Task.current_id +=1
        date_format = "%Y-%m-%d"
        self.__id = Task.current_id
        self.__desc =desc
        self.__last_time = datetime.strptime(last_time, date_format).date()
        self.__limite_time = datetime.strptime(limite_time, date_format).date()
        self.__frequency = frequency
        self.__done=done

    @property
    def desc(self):
        return self.__desc

    @property
    def done(self):
        return self.__done
    
    @property
    def id(self):
        return self.__id
    
    @property
    def last_time(self):
        return self.__last_time
    
    @property
    def limite_time(self):
        return self.__limite_time
    
    @property
    def frequency(self):
        return self.__frequency
    
    @done.setter
    def done(self,new_done):
        self.__done=new_done
    
    @last_time.setter
    def last_time(self,new_last_time):
        self.__last_time=new_last_time
    
    @limite_time.setter
    def limite_time(self,new_limite_time):
        self.__limite_time=new_limite_time
    
    @frequency.setter
    def frequency(self,new_frequency):
        self.__frequency=new_frequency
    
    @desc.setter
    def desc(self,new_desc):
        self.__desc=new_desc



    #fonction qui permet de transformer un objet TASK en un dictionaire.
    def transform_to_dico(self):
        dico={'id':self.id,'desc':self.desc,'last_time':self.last_time.strftime("%Y-%m-%d"),'limite_time':self.limite_time.strftime("%Y-%m-%d"),'frequency':self.frequency,'done':self.done}     
        return dico

    def __repr__(self):
        return('id : ' + str(self.id) + ' desc : ' + str(self.desc))

    
    