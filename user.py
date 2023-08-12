class User:

    def __init__(self, name, type):

        self.__name = name
        self.__type = type

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def connection(self, type):
        pass

    def show_tasks(self):
        pass

    def show_reward_liste(self):
        pass

    def show_scoreboard(self):
        pass

    # # fonction qui permet de transformer un objet TASK en un dictionaire.

    # def transform_to_dico(self):
    #     dico = {'name': self.name, 'status': self.status,
    #             'point': self.point, 'reward_liste': self.reward_list}
    #     return dico
