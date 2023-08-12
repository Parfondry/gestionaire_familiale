from user import User


class Parent(User):
    def __init__(self, name, type, password):

        super().__init__(name, type)

        self.passwor = password

    def add_user(self):
        pass

    def remove_user(self):
        pass

# methodes for handeling tasks

    def add_task(self):
        pass

    def remove_task(self):
        pass

    def accept_task(self):
        pass

    def reject_task(self):
        pass

    def show_requested_tasks(self):
        pass

# methodes for handeling rewards

    def add_reward(self):
        pass

    def remove_reward(self):
        pass

    def accept_reward(self):
        pass

    def reject_reward(self):
        pass

    def show_requested_reward(self):
        pass
