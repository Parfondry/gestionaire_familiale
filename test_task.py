import unittest
from datetime import datetime
from task import Task
from task_history import TaskHistory  # Import TaskHistory class if defined

class TestTask(unittest.TestCase):

    def test_task_creation(self):
        task = Task(description="Test Task", last_time="2023-08-01", limite_time="2023-08-31", point=5)
        self.assertEqual(task.description, "Test Task")
        self.assertEqual(task.point, 5)
        self.assertEqual(task.last_time, datetime(2023, 8, 1).date())
        self.assertEqual(task.limite_time, datetime(2023, 8, 31).date())

    def test_task_to_task_history(self):
        parent_task = Task(description="Parent Task", last_time="2023-08-01", limite_time="2023-08-31", point=5)
        child_task = Task(description="Child Task", last_time="2023-08-15", limite_time="2023-08-25", point=3)
        
        task_history = parent_task.task_to_task_history(child_task)
        self.assertEqual(task_history.description_task, "Parent Task")
        self.assertEqual(task_history.children, "Child Task")  
        self.assertEqual(task_history.point, 5)  # Point from parent task

    def test_transform_to_dico(self):
        task = Task(description="Test Task", last_time="2023-08-01", limite_time="2023-08-31", point=5)
        task_dict = task.transform_to_dico()
        expected_dict = {
            'description': "Test Task",
            'last_time': "2023-08-01",
            'limite_time': "2023-08-31",
            'point': 5
        }
        self.assertEqual(task_dict, expected_dict)

    def test_repr(self):
        task = Task(description="Test Task", last_time="2023-08-01", limite_time="2023-08-31", point=5)
        task_repr = repr(task)
        expected_repr = "Test Task a faire avant le 2023-08-31. Rapporte 5 points."
        self.assertEqual(task_repr, expected_repr)

if __name__ == '__main__':
    unittest.main()
