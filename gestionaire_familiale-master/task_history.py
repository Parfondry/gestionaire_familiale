

class TaskHistory:
    current_id = 0
    def __init__(self, id, description_task, date_done, user_did):
        
        self.__id = TaskHistory.current_id
        self.__description_task = description_task
        self.__date_done = date_done
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
    def id(self,new_id=True):
        self.__id=new_id
    
    @description_task.setter
    def description_task(self,new_description_task=True):
        self.__description_task=new_description_task
    
    @date_done.setter
    def date_done(self,new_date_done=True):
        self.__date_done=new_date_done

    @user_did.setter
    def user_did(self,new_user_did=True):
        self.__user_did=new_user_did
