from datetime import *
class TaskHistory:
    current_id = 0
    def __init__(self, description_task, date_done, children):
        TaskHistory.current_id += 1
        date_format = "%Y-%m-%d"
        self.__id = TaskHistory.current_id
        self.__description_task = description_task
        self.__date_done = datetime.strptime(date_done, date_format).date()
        self.__children = children

    @property
    def id(self):
        return self.__id

    @property
    def description_task(self):
        return self.__description_task

    @property
    def date_done(self):
        return self.__date_done

    @property
    def children(self):
        return self.__children

    @id.setter
    def id(self,new_id):
        self.__id=new_id

    @description_task.setter
    def description_task(self,new_description_task):
        self.__description_task=new_description_task

    @date_done.setter
    def date_done(self,new_date_done):
        self.__date_done=new_date_done

    @children.setter
    def children(self,new_children):
        self.__children=new_children

    #fonction qui permet de transformer un objet TASK en un dictionaire.
    def transform_to_dico(self):
        dico={'id':self.id,'description_task':self.description_task,'date_done':self.date_done.strftime("%Y-%m-%d"),'children':self.children}     
        return dico
    
    def __repr__(self):
        return(str(self.description_task) + " fait le " + str(self.date_done) + ". par " + str(self.children))