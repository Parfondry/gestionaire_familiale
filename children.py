

class Children:

    ongoing_tasks = [
    {"task": "Do homework", "date": "2023-08-12"},
    {"task": "Clean room", "date": "2023-08-10"},
    {"task": "Read a book", "date": "2023-08-11"}
    
    ]
    def __init__(self, name, type, points):
        super().__init__(name, type)
        self.points = points
        self.ongoing_tasks = ongoing_tasks

    def mark_task_as_completed(self):
        if not self.ongoing_tasks:
            print("No ongoing tasks available.")
            return

        print("Ongoing tasks:")
        for index, task_info in enumerate(self.ongoing_tasks, start=1):
            task = task_info["task"]
            date = task_info["date"]
            print(f"{index}. {task} (Date: {date})")

        task_choice = input("Enter the number of the task you want to go: ")
        try:
            task_choice = int(task_choice)
            if 1 <= task_choice <= len(self.ongoing_tasks):
                task_to_complete = self.ongoing_tasks[task_choice - 1]["task"]
                print(f"Do you want to mark '{task_to_complete}' as completed?")
                choice = input("1. Yes\n2. No\nYour choice: ")

                if choice == "1":
                    print(f"Task '{task_to_complete}' marked as completed.")
                    self.ongoing_tasks.pop(task_choice - 1)
                elif choice == "2":
                    print("Task not marked as completed.")
                else:
                    print("Invalid choice.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")





""" from user import User

class Children(User):
    def __init__(self, name, type, point, reward_list):
        super().__init__(name, type)
        self.__point = point
        self.__reward_list=reward_list

   
    
    @property
    def reward_list(self):
        return self.__reward_list
    
    @reward_list.setter
    def reward_list(self, new_reward_list):
        self.__reward_list= new_reward_list


    @property
    def point(self):
        return self.__point
    
    @point.setter
    def point(self, new_point):
        self.__point = new_point


    def request_task(self, task, name):
        pass

    def request_reward(self, name, date):
        pass
    
    def transform_to_dico(self):
        dico={'name':self.name,'point':self.point,'reward_list':self.reward_list}
        return dico """