from task import Task


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

    def show_tasks(self, task_liste):
        # return a list of tasks objects
        for task in task_liste:
            print(task.name + " : " + task.points)

    def show_reward_liste(self, reward_liste):
        for reward in reward_liste:
            print(reward.name + " : " + reward.cost)

    def show_scoreboard(self, children_list):
        ordered_list = sorted(
            children_list, key=lambda child: child.points, reverse=True)
        for child in ordered_list:
            print(child.name + " : " + str(child.points) + " points")

    # # fonction qui permet de transformer un objet TASK en un dictionaire.

    # def transform_to_dico(self):
    #     dico = {'name': self.name, 'status': self.status,
    #             'point': self.point, 'reward_liste': self.reward_list}
    #     return dico
