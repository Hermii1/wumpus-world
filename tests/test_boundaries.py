import unittest

from agent import Agent


class MockWorld:
    def __init__(self, agent_position, percept, valid_positions):
        self.agent_position = agent_position
        self.percept_value = percept
        self.valid_positions = valid_positions  # List of valid positions

    def percept(self):
        return self.percept_value

    def is_valid_position(self, position):
        return position in self.valid_positions


class TestAgentBoundaries(unittest.TestCase):
    def setUp(self):
        self.valid_positions = [(0, 0), (1, 0), (0, 1)]  # Define valid positions
        self.world = MockWorld((0, 0), {'stench': False, 'glitter': False, 'breeze': False}, self.valid_positions)
        self.agent = Agent(self.world)

    def test_move_within_boundaries(self):
        self.agent.move('up')  # Attempt to move to (0, 1)
        self.assertEqual(self.agent.position, (0, 1))  # Should move successfully

    def test_move_out_of_bounds(self):
        self.agent.position = (1, 0)  # Valid position
        self.agent.move('right')  # Attempting to move to (2, 0), which is invalid
        self.assertEqual(self.agent.position, (1, 0), "Agent should not move outside the grid")  # Should remain in the same position

    def test_stay_in_boundaries(self):
        self.agent.position = (0, 0)  # Start at a valid position
        self.agent.move('down')  # Attempt to move to (0, -1), which is invalid
        self.assertEqual(self.agent.position, (0, 0), "Agent should not move outside the grid")  # Should remain in the same position

if __name__ == "__main__":
    unittest.main()