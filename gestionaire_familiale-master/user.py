
class User:

    user = []

    def __init__(self, name, status, point ):

        self.__name = name
        self.__status = status
        self.__point = point

    @property
    def name(self):
        return self.__name


    @property
    def status(self):
        return self.__status

    @property
    def point(self):
        return self.__point

    @name.setter
    def name(self,new_name):
        self.__name=new_name
    
    @status.setter
    def status(self,new_status="enfant"):
        self.__status=new_status
    
    @point.setter
    def point(self,new_point=0):
        self.__point=new_point

    def connexion(self):
        pass

    def role(self):
        pass