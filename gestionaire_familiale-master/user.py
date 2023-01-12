
class User:
    current_id = 0

    def __init__(self, id, name, password, status, point ):

        self.__id = User.current_id
        self.__name = name
        self.__password = password
        self.__status = status
        self.__point = point

    @property
    def name(self):
        return self.__name

    
    @property
    def id(self):
        return self.__id

    @property
    def password(self):
        return self.__password

    @property
    def status(self):
        return self.__status

    @property
    def point(self):
        return self.__point
