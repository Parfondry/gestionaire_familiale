from datetime import *
class TaskHistory:
    current_id = 0
    def __init__(self, description_task, date_done, user_did):
        TaskHistory.current_id += 1
        date_format = "%Y-%m-%d"
        self.__id = TaskHistory.current_id
        self.__description_task = description_task
        self.__date_done = datetime.strptime(date_done, date_format).date()
        self.__user_did = user_did
    
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
    def user_did(self):
        return self.__user_did

    @id.setter
    def id(self,new_id):
        self.__id=new_id
    
    @description_task.setter
    def description_task(self,new_description_task):
        self.__description_task=new_description_task
    
    @date_done.setter
    def date_done(self,new_date_done):
        self.__date_done=new_date_done

    @user_did.setter
    def user_did(self,new_user_did):
        self.__user_did=new_user_did

    #fonction qui permet de transformer un objet TASK en un dictionaire.
    def transform_to_dico(self):
        dico={'id':self.id,'description_task':self.description_task,'date_done':self.date_done.strftime("%Y-%m-%d"),'user_did':self.user_did}     
        return dico