import unittest
from gol import *

class MyTestCase(unittest.TestCase):
    
    def test_create_world(self):
        #Given
        game = myapp()
        #When
        game.create_world()
        #Then
        self.assertTrue(game.world_exists())

if __name__ == '__main__':
    unittest.main()