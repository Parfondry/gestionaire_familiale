
class Reward:

    def __init__(self, cost_point, name):
        
        self.__cost_point = cost_point
        self.__name = name
    
    @property
    def cost_point(self):
        return self.__cost_point

    @property
    def name(self):
        return self.__name

    @cost_point.setter
    def cost_point(self,cost_point):
        self.__cost_point=cost_point

    @name.setter
    def name(self,name):
        self.__name=name

    #fonction qui permet de transformer un objet TASK en un dictionaire.
    def transform_to_dico(self):
        dico={'name':self.name,'cost_point':self.cost_point}     
        return dico