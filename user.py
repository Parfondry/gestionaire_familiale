
class User:
    def __init__(self, name):
        self.__name = name
        self.points = 0

    @property
    def name(self):
        return self.__name

    def earn_points(self, pts):
        self.points += pts

    def get_tasks(self, task_list):
        return [f"{task.name} : {task.points}" for task in task_list]

    def get_rewards(self, reward_list):
        return [f"{reward.name} : {reward.cost}" for reward in reward_list]

    def get_scoreboard(self, children_list):
        ordered_list = sorted(
            children_list, key=lambda child: child.points, reverse=True)
        return [f"{child.name} : {child.points} points" for child in ordered_list]
