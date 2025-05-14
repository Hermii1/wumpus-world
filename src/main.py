from wumpus_world import WumpusWorld  # Ensure this line is correct
from agent import Agent

def move_agent(agent, direction):
    # Implement movement logic based on direction
    if direction == 'up':
        agent.position = (agent.position[0], agent.position[1] - 1)
    elif direction == 'down':
        agent.position = (agent.position[0], agent.position[1] + 1)
    elif direction == 'left':
        agent.position = (agent.position[0] - 1, agent.position[1])
    elif direction == 'right':
        agent.position = (agent.position[0] + 1, agent.position[1])
    
    # Here you can add checks for Wumpus, pits, and update the game state
    # For example:
    if agent.position in agent.world.pits:
        print("The agent fell into a pit! Game over.")
        return False  # End the game
    elif agent.position == agent.world.wumpus_position:
        print("The agent encountered the Wumpus! Game over.")
        return False  # End the game
    elif agent.position == agent.world.gold_position:
        print("The agent found the gold! You win!")
        return False  # End the game
    
    return True  # Continue the game


def run_simulation():
    world = WumpusWorld()  # Use WumpusWorld without underscore
    agent = Agent(world)
    # Add your simulation logic here
    print("Initial State:")
    print("Agent position:", agent.position)
    print("Wumpus position:", world.wumpus_position)
    print("Pits:", world.pits)
    print("Gold position:", world.gold_position)

    while True:
        direction = input("Enter direction (up, down, left, right) or 'exit' to quit: ")
        if direction == 'exit':
            break
        
        # Move the agent and check game status
        if not move_agent(agent, direction):
            break  # Exit the loop if the game is over
        
        print("Agent position after moving:", agent.position)


if __name__ == "__main__":
    run_simulation()