import unittest
from CardRace import Database


class UnitTesting(unittest.TestCase):

    def test(self):
        self.assertEqual(Database.allUsers("users.csv"), ["abe"])
        self.assertEqual(Database.add_Users("users.csv", "abe"), ["abe"])
        self.assertEqual(Database.add_Users("users.csv", "abe"), ["abe"])
        self.assertEqual(Database.allUsers("users.csv"), ["abe"])
        self.assertEqual(Database.add_Users("users.csv", "sad"), ["abe", "sad"])
        self.assertEqual(Database.allUsers("users.csv"), ["abe", "sad"])
        self.assertEqual(Database.add_Users("users.csv", ""), ["abe", "sad"])
        self.assertEqual(Database.allUsers("users.csv"), ["abe", "sad"])


if __name__ == '__main__':
    unittest.main()