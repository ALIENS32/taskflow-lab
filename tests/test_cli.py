import unittest
from pathlib import Path
from taskflow.cli import load_tasks, save_tasks

class TestTaskflow(unittest.TestCase):
    def test_load_save(self):
        d = Path("/tmp/test_tasks.json")
        if d.exists():
            d.unlink()
        import taskflow.cli
        taskflow.cli.DATA_FILE = d
        self.assertEqual(load_tasks(), [])
        save_tasks([{"id": 1, "title": "test", "completed": False}])
        self.assertEqual(len(load_tasks()), 1)
        if d.exists():
            d.unlink()

if __name__ == "__main__":
    unittest.main()
