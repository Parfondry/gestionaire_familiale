
class User:

    def __init__(self, name):

        self.__name = name

    @property
    def name(self):
        return self.__name


    def get_tasks(self, task_liste):
        # return a list of tasks objects
        for task in task_liste:
            print(task.name + " : " + task.points)

    def get_rewards(self, reward_liste):
        for reward in reward_liste:
            print(reward.name + " : " + reward.cost)

    def get_scoreboard(self, children_list):
        ordered_list = sorted(
            children_list, key=lambda child: child.points, reverse=True)
        for child in ordered_list:
            print(child.name + " : " + str(child.points) + " points")

 