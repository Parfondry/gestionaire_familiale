from datetime import *

class Task:
    
    def __init__(self, name, point, last_time_done, time_limit):
        self.name = name
        date_format = "%Y-%m-%d"
        self.point = point
        self.last_time_done =  datetime.strptime(last_time_done, date_format).date()
        self.time_limit = datetime.strptime(time_limit, date_format).date()


    @property
    def point(self):
        return self.point    
    
    @point.setter
    def point(self, new_point):
        self.point = new_point

    


    #fonction qui permet de transformer un objet TASK en un dictionaire.
   # def transform_to_dico(self):
    #    dico={'id':self.id,'desc':self.desc,'last_time':self.last_time.strftime("%Y-%m-%d"),'limite_time':self.limite_time.strftime("%Y-%m-%d"),'frequency':self.frequency,'done':self.done}     
     #   return dico

    #def __repr__(self):
     #   return('id : ' + str(self.id) + ' desc : ' + str(self.desc))
