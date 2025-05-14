from wumpus_world import WumpusWorld  # Ensure this line is correct
from agent import Agent

class Agent:
    def init(self):
        self.position = (0, 0)  # Starting position

    def move(self, direction):
        if direction == "up":
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == "down":
            self.position = (self.position[0], self.position[1] - 1)
        # Add more directions as needed

def test_agent_movement():
    agent = Agent()
    print("Starting position:", agent.position)

    # Test moving up
    agent.move("up")
    print("Position after moving up:", agent.position)

    # Test moving down
    agent.move("down")
    print("Position after moving down:", agent.position)

    # You can add more tests here

# Run the test
if __name__ == "main":
    test_agent_movement()