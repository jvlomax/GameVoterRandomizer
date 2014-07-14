__author__ = 'george'
import unittest
from database import GamesHandler

class TestGamesDatabseFunctions(unittest.TestCase):

    def setUp(self):
        self.db = GamesHandler("testDb.sql")

    def test_add_game(self):
        self.db.add_game("Unreal Tournament")
        all = self.db.get_all()
        self.assertEqual(all, [(1, "Unreal Tournament", "[]", 0)])

    def test_primary_keys(self):
        self.db.add_game("Unreal Tournament")
        self.db.add_game("Ra2")
        self.db.add_game("The sims")
        all = self.db.get_all()
        ut = all[0][0]
        ra2 = all[1][0]
        sims = all[2][0]

        self.assertEqual(ut, 1)
        self.assertEqual(ra2, 2)
        self.assertEqual(sims, 3)
    def test_add_like(self):
        self.db.add_game("Unreal Tournament")
        self.db.add_like("Unreal Tournament", "kalle")
        all = self.db.get_all()
        self.assertEqual(all, [(1, "Unreal Tournament", "['kalle']", 1)])

    def test_remove_like(self):
        self.db.add_game("Unreal Tournament")
        self.db.add_like("Unreal Tournament", "kalle")
        all = self.db.get_all()
        self.assertEqual(all, [(1, "Unreal Tournament", "['kalle']", 1)])
        self.db.remove_like("Unreal Tournament", "kalle")
        all = self.db.get_all()
        self.assertEqual(all, [(1, "Unreal Tournament", "[]", 0)])

    def test_update(self):
        pass

class TestCookieDatabaseFunctions:
    pass
if __name__ == "__main__":
     unittest.main()