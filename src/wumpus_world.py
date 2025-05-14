import random

class WumpusWorld:
    def __init__(self):
        self.size = 4
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.agent_position = (0, 0)
        self.pits = []  # Initialize pits
        self.wumpus_position = None  # Initialize wumpus_position
        self.gold_position = None  # Initialize gold_position
        self.place_features()
        self.valid_positions = [(0, 0), (1, 0), (0, 1)]  # Example valid positions
    def is_valid_position(self, position):
        # Check if the position is within valid bounds
        if position in self.valid_positions:
            return True
        return False
    def get_invalid_positions(self):
        # Define the full grid and return invalid positions
        all_possible_positions = [(x, y) for x in range(3) for y in range(3)]  # Example 3x3 grid
        return [pos for pos in all_possible_positions if pos not in self.valid_positions]
    def place_features(self):
        # Place Wumpus
        self.wumpus_position = self.random_empty_cell()
        self.grid[self.wumpus_position[0]][self.wumpus_position[1]] = 'W'

        # Place pits
        self.pits = [self.random_empty_cell() for _ in range(3)]
        for pit in self.pits:
            self.grid[pit[0]][pit[1]] = 'P'
        
        # Place gold
        self.gold_position = self.random_empty_cell()
        self.grid[self.gold_position[0]][self.gold_position[1]] = 'G'

    def random_empty_cell(self):
        while True:
            cell = (random.randint(0, 3), random.randint(0, 3))
            if cell != self.agent_position and cell not in self.pits and cell != self.wumpus_position:
                return cell

    def percept(self):
        # Returns percepts based on the current position
        x, y = self.agent_position
        percepts = {}
        # Check for stench
        percepts['stench'] = self.is_adjacent_to_wumpus(x, y)
        # Check for breeze
        percepts['breeze'] = self.is_adjacent_to_pits(x, y)
        # Check for glitter
        percepts['glitter'] = self.agent_position == self.gold_position
        return percepts

    def is_adjacent_to_wumpus(self, x, y):
        return any((nx, ny) == self.wumpus_position for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)])

    def is_adjacent_to_pits(self, x, y):
        return any((nx, ny) in self.pits for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)])

    # Additional methods for moving the agent, updating the grid, etc.