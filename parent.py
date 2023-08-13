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

    def add_child(self, child_name, data):
        if child_name not in data.list_children:
            new_child = Children(child_name, 0)
            data.add_children(new_child)
        else:
            print("Il exixste déja un enfant avec le nom " + child_name)

    def remove_children(self, child, data):
        if child not in data.list_children:
            print("Il n'existe pas d'enfant avec le nom " + child.name)
        else:
            data.list_children.remove(child)

# methodes for handeling tasks

    def add_task(self, task_name, points, last_time_done, time_limit, data):
        if task_name not in data.list_task:
            new_task = Task(task_name, points, last_time_done, time_limit)
            data.add_task(new_task)
        else:
            print("Il exixste déja une tache : " + task_name)

    def remove_task(self, task, data):
        if task in data.list_task:
            data.list_task.remove(task)

    def accept_task(self, task, child, data):
        DataManager.add_task_to_be_validated.remove(task)
        DataManager.add_task_history.append(task)
        child.points += task.points

    def reject_task(self, task):
        DataManager.add_task_to_be_validated.remove(task)

    def show_requested_tasks(self):
        task_liste = []
        for task in DataManager.list_task_to_validated:
            task_liste.append(task)
        return task_liste


# methodes for handeling rewards

    def add_reward(self, reward_name, cost):
        if reward_name not in DataManager.list_reward.name:
            new_reward = Reward(reward_name, cost)
            DataManager.add_reward(new_reward)
        else:
            print("Il exixste déja une récompense : " + reward_name)

    def remove_reward(self, reward):
        if reward in DataManager.list_reward:
            DataManager.list_reward.remove(reward)

    def accept_reward(self, reward, child):
        DataManager.list_reward_to_be_granted.remove(reward)
        child.points = child.points - reward.cost

    def reject_reward(self, reward):
        DataManager.list_reward_to_be_granted.remove(reward)

    def show_requested_reward(self):
        reward_liste = []
        for reward in DataManager.list_reward_to_be_granted:
            reward_liste.append(reward)
        return reward_liste
