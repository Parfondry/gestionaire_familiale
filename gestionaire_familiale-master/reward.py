
class Reward:

    def __init__(self, cost_point, reward_name):
        
        self.__cost_point = cost_point
        self.__reward_name = reward_name
    
    @property
    def cost_point(self):
        return self.__cost_point

    @property
    def name(self):
        return self.__reward_name