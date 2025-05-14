class Agent:
    def __init__(self, world):
        self.world = world
        self.position = world.agent_position
        self.has_gold = False
        self.health = 1  # 1 means alive, 0 means dead

    def perceive(self):
        return self.world.percept()

    def decide_action(self, percept):
        if percept['glitter']:
            return 'grab'
        elif percept['stench']:
            return 'avoid'
        elif percept['breeze']:  # Assuming breeze indicates a pit nearby
            return 'avoid'
        else:
            return 'move'

    def act(self ):
        percept = self.perceive()
        action = self.decide_action(percept)
        print(f"Action decided: {action}")
    
        if action == 'grab':
            self.has_gold = True
            print("Gold grabbed!")
        elif action == 'avoid':
            self.handle_encounter(percept)
        elif action == 'move':
            self.move('up')  # Specify a default direction to move. Change as needed.

    def handle_encounter(self, percept):
        if percept['stench']:
            self.encounter_wumpus()
        elif percept['breeze']:
            self.fall_into_pit()
    def move(self ,direction ):
        
        if direction not in ['up', 'down', 'left', 'right']:
            raise ValueError("Invalid direction!")
    
        # Example implementation for direction-based movement
        if direction == 'up':
            new_position = (self.position[0], self.position[1] + 1)
        elif direction == 'down':
            new_position = (self.position[0], self.position[1] - 1)
        elif direction == 'left':
            new_position = (self.position[0] - 1, self.position[1])
        elif direction == 'right':
            new_position = (self.position[0] + 1, self.position[1])
        else:
            return  # Invalid direction

        if self.world.is_valid_position(new_position):
            self.position = new_position
            print(f"Moved to {self.position}")
        else:
            print("Invalid move!")      

    def encounter_wumpus(self):
        self.health = 0  # Wumpus kills the agent

    def fall_into_pit(self):
        self.health = 0  # Pit kills the agent

    def is_alive(self):
        return self.health > 0