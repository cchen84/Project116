import unittest
import pygame.tests
from CardRace import Database,game

class TheTest(unittest.TestCase):
    def test_get_pressed(self):
        self.assertEqual(pygame.tests.run(game.game_loop()))
        self.assertEqual(Database.add_Users("users.csv", "abe"), ["abe"])
        self.assertEqual(Database.allUsers("users.csv"), ["abe"])
        self.assertEqual(Database.add_Users("users.csv", "sad"), ["abe", "sad"])
        self.assertEqual(Database.allUsers("users.csv"), ["abe", "sad"])
        self.assertEqual(Database.add_Users("users.csv", ""), ["abe", "sad"])
        self.assertEqual(Database.allUsers("users.csv"), ["abe", "sad"])

if __name__ == '__main__':
    unittest.main()