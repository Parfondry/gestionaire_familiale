class User:

    def __init__(self, name, status, point , reward_list ):

        self.__name = name
        self.__status = status
        self.__point = point
        self.__reward_list = reward_list

    @property
    def name(self):
        return self.__name

    @property
    def reward_list(self):
        return self.__reward_list

    @property
    def status(self):
        return self.__status

    @property
    def point(self):
        return self.__point

    @name.setter
    def name(self,new_name):
        self.__name=new_name
    
    @reward_list.setter
    def reward_list(self,reward_list):
        self.__reward_list=reward_list
    
    
    @status.setter
    def status(self,new_status="enfant"):
        self.__status=new_status
    
    @point.setter
    def point(self,new_point=0):
        self.__point=new_point

    #fonction qui permet de transformer un objet TASK en un dictionaire.
    def transform_to_dico(self):
        dico={'name':self.name,'status':self.status,'point':self.point,'reward_liste':self.reward_list}     
        return dico

    