from parent import Parent
from children import Children
from task import Task
from reward import Reward
from datamanager import DataManager
import unittest


class TestParent(unittest.TestCase):
    def setUp(self):
        self.parent = Parent("John", "password123")

        self.data = DataManager()

        self.data.list_children = [Children("Alice"), Children("Bob")]

        self.data.list_task = [Task("Clean room", "2023-01-01", "2023-01-15", 10),
                               Task("Do homework", "2023-01-01", "2023-01-07", 20)]

        self.data.list_task_to_be_validated = [
            Task("Wash dishes", "2023-01-02", "2023-01-05", 5)]

        self.data.list_reward = [Reward("Ice cream", 5), Reward("New toy", 15)]

        self.data.list_task_history = [
            Task("Take out trash", "2023-01-01", "2023-01-03", 3)]

        self.data.list_reward_to_be_granted = [
            Reward("1 hour of video games", 10)]

    def test_add_child(self):
        self.parent.add_child("Alice", self.data)
        self.assertIn(
            "Alice", [child.name for child in self.data.list_children])

    def test_add_existing_child(self):
        self.parent.add_child("Alice", self.data)
        self.parent.add_child("Alice", self.data)  # This should print an error

    def test_remove_child(self):
        child = Children("Alice")
        self.data.list_children.append(child)
        self.parent.remove_children(child, self.data)
        self.assertNotIn(child, self.data.list_children)

    def test_add_task(self):
        self.parent.add_task("Clean room", "2023-01-01",
                             "2023-01-15", 10, self.data)
        self.assertIn(
            "Clean room", [task.description for task in self.data.list_task])

    def test_remove_task(self):
        task = Task("Clean room", "2023-01-01", "2023-01-15", 10)
        self.data.list_task.append(task)
        self.parent.remove_task(task, self.data)
        self.assertNotIn(task, self.data.list_task)

    # Plus de tests pour les autres méthodes...


if __name__ == '__main__':
    unittest.main()
