from datamanager import DataManager
from datetime import datetime
from parent import Parent
from task_history import TaskHistory
data = DataManager()
data.load_data()

data.show_list_task()
print("--")
data.show_list_reward()
print("--")
data.show_list_reward_to_be_granted()
print("--")
data.show_list_task_history()
print("--")
data.show_list_task_to_be_validated()
print("--")
data.show_list_children()
print("--")
l=data.list_task_to_be_validated[2]
data.list_task_to_be_validated.remove(l)
data.show_list_task_to_be_validated()