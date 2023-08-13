from user import User
import unittest


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Alice")
        self.task1 = type('Task', (), {"name": "Task1", "points": 10})
        self.task2 = type('Task', (), {"name": "Task2", "points": 20})
        self.reward1 = type('Reward', (), {"name": "Reward1", "cost": 5})
        self.reward2 = type('Reward', (), {"name": "Reward2", "cost": 15})

    def test_name(self):
        self.assertEqual(self.user.name, "Alice")

    def test_earn_points(self):
        self.user.earn_points(10)
        self.assertEqual(self.user.points, 10)
        self.user.earn_points(20)
        self.assertEqual(self.user.points, 30)

    def test_get_tasks(self):
        tasks = self.user.get_tasks([self.task1, self.task2])
        self.assertEqual(tasks, ["Task1 : 10", "Task2 : 20"])

    def test_get_rewards(self):
        rewards = self.user.get_rewards([self.reward1, self.reward2])
        self.assertEqual(rewards, ["Reward1 : 5", "Reward2 : 15"])

    def test_get_scoreboard(self):
        user2 = User("Bob")
        user2.earn_points(50)
        scoreboard = self.user.get_scoreboard([self.user, user2])
        self.assertEqual(scoreboard, ["Bob : 50 points", "Alice : 0 points"])


if __name__ == '__main__':
    unittest.main()
