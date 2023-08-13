from user import User
from datamanager import DataManager
from children import Children
from task import Task
from reward import Reward


class Parent(User):
    def __init__(self, name, password):

        super().__init__(name)
        self.type = 0

        self.passwor = password

    def add_child(self, child_name):
        if child_name not in DataManager.list_children:
            new_child = Children(child_name, 0)
            DataManager.add_children(new_child)
        else:
            print("Il exixste déja un enfant avec le nom " + child_name)

    def remove_child(self, child_name):
        if child_name not in DataManager.list_children:
            print("Il n'existe pas d'enfant avec le nom " + child_name)
        else:
            pass

# methodes for handeling tasks

    def add_task(self, task_name, points, last_time_done, time_limit):
        if task_name not in DataManager.list_task:
            new_task = Task(task_name, points, last_time_done, time_limit)
            DataManager.add_task(new_task)
        else:
            print("Il exixste déja une tache : " + task_name)

    def remove_task(self):
        pass

    def accept_task(self):
        pass

    def reject_task(self):
        pass

    def show_requested_tasks(self):
        pass

# methodes for handeling rewards

    def add_reward(self, reward_name, cost):
        if reward_name not in DataManager.list_reward:
            new_reward = Reward(reward_name, cost)
            DataManager.add_reward(new_reward)
        else:
            print("Il exixste déja une récompense : " + task_name)

    def remove_reward(self):
        pass

    def accept_reward(self):
        pass

    def reject_reward(self):
        pass

    def show_requested_reward(self):
        pass
