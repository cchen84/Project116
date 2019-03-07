import unittest
import pygame

from CardRace import client

class Test(unittest.TestCase):

    def test_move(self):

        left = client.Player.move(self.left)
        self.assertEqual(left, pygame.K_RIGHT)



    if __name__ == '__main__':
        unittest.main()

