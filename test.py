from datamanager import DataManager
from datetime import datetime

 ### test de launch

launch=DataManager(['a'],2,3,4,5,6)
print(launch.list_task)
launch.load_data()
print(launch.list_task)
print(launch.list_reward[0].name)
print(launch.list_children[0].name)
print(launch.list_task_history[0].description_task)
print(launch.list_reward_to_be_granted[0])
print(launch.list_task_to_validated[0])

### test de task_done, transformer une task en task history

task_to_transform = launch.list_task[0]
children=launch.list_children[0]
print(task_to_transform)
print(children.name)
print(datetime.now())
task_history_created=task_to_transform.task_done(children)
print(task_history_created)
print(task_history_created.description_task)

launch.write_data()