import unittest
from src import manager


# in root dir, python -m unittest tests.test_manager


class TestManager(unittest.TestCase):

    def setUp(self):
        # Reset MANAGER and SEEN_NAMES before each test
        manager.MANAGER.clear()
        manager.SEEN_NAMES.clear()

    def test_create_group(self):
        group_name = "test_group"
        result = manager.create_group(group_name)
        self.assertIsNotNone(result)
        self.assertIn(group_name, manager.MANAGER)
        self.assertEqual(manager.MANAGER[group_name]["name"], group_name)

    def test_create_group_existing_name(self):
        group_name = "test_group"
        manager.create_group(group_name)
        result = manager.create_group(group_name)
        self.assertIsNone(result)

    def test_search_group(self):
        group_name = "test_group"
        manager.create_group(group_name)
        result = manager.search_group(group_name)
        self.assertTrue(result)
        self.assertFalse(manager.search_group("non_existing_group"))

    def test_delete_group(self):
        group_name = "test_group"
        manager.create_group(group_name)
        result = manager.delete_group(group_name)
        self.assertIsNotNone(result)
        self.assertNotIn(group_name, manager.MANAGER)

    def test_delete_group_non_existing(self):
        group_name = "test_group"
        result = manager.delete_group(group_name)
        self.assertIsNone(result)

    def test_add_pass(self):
        group_name = "test_group"
        manager.create_group(group_name)
        result = manager.add_pass(group_name, "id1", "password1")
        self.assertIn("id1", manager.MANAGER[group_name]["passwords"])
        self.assertEqual(manager.MANAGER[group_name]["passwords"]["id1"], "password1")

    def test_add_pass_existing_id(self):
        group_name = "test_group"
        manager.create_group(group_name)
        manager.add_pass(group_name, "id1", "password1")
        result = manager.add_pass(group_name, "id1", "password2")
        self.assertEqual(manager.MANAGER[group_name]["passwords"]["id1"], "password1")

    def test_search_id(self):
        group_name = "test_group"
        manager.create_group(group_name)
        manager.add_pass(group_name, "id1", "password1")
        self.assertTrue(manager.search_id(group_name, "id1"))
        self.assertFalse(manager.search_id(group_name, "id2"))

    def test_search_id_non_existing_group(self):
        self.assertFalse(manager.search_id("non_existing_group", "id1"))

    def test_delete_pass(self):
        group_name = "test_group"
        manager.create_group(group_name)
        manager.add_pass(group_name, "id1", "password1")
        result = manager.delete_pass(group_name, "id1")
        self.assertNotIn("id1", manager.MANAGER[group_name]["passwords"])
        self.assertEqual(result[1], "password1")

    def test_delete_pass_non_existing(self):
        group_name = "test_group"
        manager.create_group(group_name)
        result = manager.delete_pass(group_name, "id1")
        self.assertEqual(result, (manager.MANAGER[group_name], None))


if __name__ == "__main__":
    unittest.main()
