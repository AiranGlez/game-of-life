import unittest
from gol import *


class MyTestCase(unittest.TestCase):

    def test_create_world(self):
        #Given
        game = Gol()
        #When
        rows = 4
        columns = 6
        game.create_world(rows, columns)
        #Then
        self.assertTrue(game.world_exists())

    def test_populate_world(self):
        #Given
        game = Gol()
        #When
        rows = 4
        columns = 6
        game.create_world(rows, columns)
        game.populate_world()
        #Then
        self.assertTrue(game.world_is_populated())

if __name__ == '__main__':
    unittest.main()