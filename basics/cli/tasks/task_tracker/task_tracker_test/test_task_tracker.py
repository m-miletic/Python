import unittest
import tempfile
from pathlib import Path
from task_tracker import Task, load_tasks, save_tasks
from datetime import datetime
import json

target = __import__("task_tracker")
add_task = target.add_task
load_tasks = target.load_tasks
update_task = target.update_task
delete_task = target.delete_task

class TestTaksTracker(unittest.TestCase):
    # Testing load_tasks() function
    # check if the file exists ?
    # if true: does it correctly load the tasks ?
    # if false: does it return an empty list ?
    """
    Test that function return asn empty list when file does not exist
    """
    def test_load_tasks_file_does_not_exist(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            # Arrange
            target.FILE = Path(temp_dir) / "tasks.json"
            # Act
            tasks = load_tasks()
            # Assert 
            self.assertEqual(tasks, [])

    """
    Tests that function corectly loads tasks from an existing JSON file
    """
    def test_load_tasks_existing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            # Arrange
            target.FILE = Path(temp_dir) / "tasks.json"

            tasks_data = [
                {
                    "id": 1,
                    "description": "Learn unittest",
                    "status": "TODO",
                    "created_at": "2026-08-18 10:00:00",
                    "updated_at": "2026-08-18 10:00:00"
                }
            ]

            with target.FILE.open("w") as file:
                json.dump(tasks_data, file, indent=4)

            # Act
            tasks = load_tasks()
            # Assert
            self.assertEqual(tasks, tasks_data)


    def test_add_task(self):
        """
        Test that it can add a new task
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            target.FILE = Path(temp_dir) / "tasks.json" # Arrange

            add_task("Learn unittest") # Act

            tasks = load_tasks()

            # Assert
            self.assertEqual(len(tasks), 1)
            self.assertEqual(tasks[0]["description"], "Learn unittest")
            self.assertEqual(tasks[0]["status"], "TODO")
            self.assertEqual(tasks[0]["id"], 1)

    def test_update_task(self):
        """
        Test that it can update the existing task
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            # Arrange
            target.FILE = Path(temp_dir) / "tasks.json"

            task = Task(
                1,
                "Learn programming",
                "TODO",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

            # Put test task into the temporary JSON file
            save_tasks([task.__dict__])

            # Act
            update_task(1, "Learn unit testing")

            # Assert
            tasks = load_tasks()

            self.assertEqual(tasks[0]["id"], 1)
            self.assertEqual(tasks[0]["description"], "Learn unit testing")


    # Testing delete_task() function
    # Does taks with id exist ?
    # if true: delete it
    # if false: give error
    def test_delete(self):
        """
        Test that it can delete and existing task
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            target.FILE = Path(temp_dir) / "tasks.json"

            task = Task(
                1,
                "Task which I'm going to delete",
                "TODO",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

            # Put test task into the temporary JSON file
            save_tasks([task.__dict__])

            delete_task(1)

            tasks = load_tasks()

            self.assertEqual(len(tasks), 0)
            



