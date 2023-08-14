from datamanager import DataManager
from datetime import datetime
from parent import Parent
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
data.show_list_task_to_validated()
print("--")
data.show_list_children()