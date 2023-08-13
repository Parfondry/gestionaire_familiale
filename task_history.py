from datetime import *


class TaskHistory:
    #current_id = 0
    def __init__(self, name , children, date_done):
        #TaskHistory.current_id += 1
        date_format = "%Y-%m-%d"
        #self.__id = TaskHistory.current_id
        self.__name = name
        self.__date_done = datetime.strptime(date_done, date_format).date()
        self.__children = children
    
    #@property
    #def id(self):
     #   return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def date_done(self):
        return self.__date_done

#    @id.setter
 #   def id(self,new_id):
  #      self.__id=new_id
    
    @name.setter
    def name(self,new_name):
        self.__name=new_name
    
    @date_done.setter
    def date_done(self,new_date_done):
        self.__date_done=new_date_done

    #fonction qui permet de transformer un objet TASK en un dictionaire.
   # def transform_to_dico(self):
      #  dico={'id':self.id,'description_task':self.description_task,'date_done':self.date_done.strftime("%Y-%m-%d"),'user_did':self.user_did}     
       # return dico