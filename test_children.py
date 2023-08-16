from children import Children
from task import Task
from reward import Reward
from datamanager import DataManager
import unittest


class TestChildren(unittest.TestCase):
    def setUp(self):
        self.child = Children("Alice")
        self.data = DataManager()

        self.data.list_task_to_be_validated = [
            Task("Wash dishes", "2023-01-02", "2023-01-05", 5)]

        self.task = Task("Clean room", "2023-01-01", "2023-01-15", 10)
        self.reward = Reward("Ice cream", 5)

    def test_point_property(self):
        self.child.point = 10
        self.assertEqual(self.child.point, 10)

    def test_reward_list_property(self):
        self.child.reward_list = ["Ice cream", "New toy"]
        self.assertListEqual(self.child.reward_list, ["Ice cream", "New toy"])

    def test_transform_to_dico(self):
        dico = self.child.transform_to_dico()
        self.assertDictEqual(
            dico, {'name': 'Alice', 'point': 0, 'reward_list': []})

    def test_repr(self):
        self.assertEqual(repr(self.child), "Alice possède 0 points")


if __name__ == '__main__':
    unittest.main()
