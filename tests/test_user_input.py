# test/test_user_input.py

import unittest
from wumpus_world import WumpusWorld
from agent import Agent

class TestUserInput(unittest.TestCase):

    def setUp(self):
        self.world = WumpusWorld()
        self.agent = Agent(self.world)

    def test_invalid_input(self):
        invalid_commands = ["north", "southwest", "upward"]
        for command in invalid_commands:
            with self.assertRaises(ValueError):
                self.agent.move(command)

if __name__ == '__main__':
    unittest.main()