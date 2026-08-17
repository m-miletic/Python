import unittest
import tempfile
from pathlib import Path


target = __import__("task_tracker")
add_task = target.add_task


class TestTaksTracker(unittest.TestCase):
    def test_add_task(self):
        """
        Test that it can add a new task
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            target.FILE = Path(temp_dir) / "tasks.json" # Arrange

            add_task("Learn unittest") # Act

            tasks = target.load_tasks()

            # Assert
            self.assertEqual(len(tasks), 1)
            self.assertEqual(tasks[0]["description"], "Learn unittest")
            self.assertEqual(tasks[0]["status"], "TODO")
            self.assertEqual(tasks[0]["id"], 1)

