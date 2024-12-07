import unittest
import json
from Project import load_tasks, save_tasks, add_task, complete_task

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # Prepare a fresh tasks list for each test
        self.tasks = [
            {"description": "Sample Task 1", "deadline": "2024-12-10", "completed": False},
            {"description": "Sample Task 2", "deadline": "None", "completed": False}
        ]

    def test_load_tasks(self):
        # Test loading tasks from a file
        with open("test_tasks.json", "w") as file:
            json.dump(self.tasks, file)
        
        loaded_tasks = load_tasks()
        self.assertEqual(loaded_tasks, self.tasks)

    def test_save_tasks(self):
        # Test saving tasks to a file
        save_tasks(self.tasks)
        with open("tasks.json", "r") as file:
            saved_tasks = json.load(file)
        self.assertEqual(saved_tasks, self.tasks)

    def test_add_task(self):
        # Test adding a task
        description = "New Task"
        deadline = "2024-12-15"
        self.tasks.append({"description": description, "deadline": deadline, "completed": False})
        self.assertEqual(len(self.tasks), 3)
        self.assertEqual(self.tasks[-1]["description"], description)

    def test_complete_task(self):
        # Test marking a task as complete
        self.tasks[0]["completed"] = True
        self.assertTrue(self.tasks[0]["completed"])

if __name__ == "__main__":
    unittest.main()
