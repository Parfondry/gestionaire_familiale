from user import User
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
            new_child = Children(child_name)
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

    def accept_task(self, task_history, child, data):
        data.list_task_to_be_validated.remove(task_history)
        data.add_task_history(task_history)
        child.point += task_history.point
        for task in data.list_task:
            if task.description==task_history.description_task:
                task.last_time=task_history.date_done

    def reject_task(self, task,data):
        data.list_task_to_be_validated.remove(task)
    

# methodes for handeling rewards

    def add_reward(self, reward, cost, data):
        if reward not in data.list_reward:
            new_reward = Reward(reward.name, cost)
            data.add_reward(new_reward)
        else:
            print("Il existe déja une récompense : " + reward.name)

    def remove_reward(self, reward, data):
        if reward in data.list_reward:
            data.list_reward.remove(reward)

    def accept_reward(self, reward, child,data):
        data.list_reward_to_be_granted.remove(reward)
        child.points = child.points - reward.cost
        child.reward_list.add(reward)

    def reject_reward(self, reward, data):
        data.list_reward_to_be_granted.remove(reward)
