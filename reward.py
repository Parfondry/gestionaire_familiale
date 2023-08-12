
class Reward:

    def __init__(self, cost, name):

        self.__cost_point = cost
        self.__name = name

    @property
    def cost(self):
        return self.__cost

    @property
    def name(self):
        return self.__name

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @name.setter
    def name(self, name):
        self.__name = name

    # #fonction qui permet de transformer un objet TASK en un dictionaire.
    # def transform_to_dico(self):
    #     dico={'name':self.name,'cost_point':self.cost_point}
    #     return dico
