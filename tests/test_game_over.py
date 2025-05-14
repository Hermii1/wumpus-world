import unittest

from agent import Agent



class MockWorld:
    def __init__(self, agent_position, percept, valid_positions=None):
        self.agent_position = agent_position
        self.percept_value = percept
        self.valid_positions = valid_positions if valid_positions is not None else [(0, 0), (1, 0), (0, 1)]

    def percept(self):
        return self.percept_value

    def is_valid_position(self, position):
        return position in self.valid_positions


class TestAgent(unittest.TestCase):
    def test_game_over_wumpus(self):
        world = MockWorld((0, 0), {'stench': True, 'glitter': False, 'breeze': False})
        agent = Agent(world)

        agent.act()  # Should encounter the Wumpus
        self.assertFalse(agent.is_alive())  # Should be dead after encounter

    def test_game_over_pit(self):
        world = MockWorld((0, 0), {'breeze': True, 'stench': False, 'glitter': False})
        agent = Agent(world)

        agent.act()  # Should fall into a pit
        self.assertFalse(agent.is_alive())  # Should be dead after falling

    def test_alive_after_safe_move(self):
        world = MockWorld((0, 0), {'stench': False, 'glitter': False, 'breeze': False})
        agent = Agent(world)

        agent.act()  # Should move safely
        self.assertTrue(agent.is_alive())  # Should still be alive


if __name__ == "__main__":
    unittest.main()