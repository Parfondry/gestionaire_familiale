

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
