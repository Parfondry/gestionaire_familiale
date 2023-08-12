from user import User


class Children(User):
    def __init__(self, name, type, points):
        super().__init__(name, type)
        self.points = points

    def request_task(self, task, name):
        pass

    def request_reward(self, name, date):
        pass
