from datamanager import DataManager


launch=DataManager(['a'],2,3,4,5,6)
print(launch.list_task)
launch.load_data()
print(launch.list_task)
print(launch.list_reward[0].name)
print(launch.list_children[0].name)
print(launch.list_task_history[0].description_task)
print(launch.list_reward_to_be_granted[0])
print(launch.list_task_to_validated[0])


launch.write_data()