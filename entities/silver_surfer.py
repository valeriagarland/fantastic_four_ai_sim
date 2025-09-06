
import random
from environment.cell import CellType

class SilverSurfer:
    def __init__(self, x, y, grid, energy=100):
        self.x = x
        self.y = y
        self.grid = grid
        self.energy = energy
        self.max_energy = 100
        self.active = True

    def move(self):
        if not self.active:
            return

        # Moves faster: 2 steps per turn
        for _ in range(2):
            dx, dy = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
            self.x = (self.x + dx) % self.grid.width
            self.y = (self.y + dy) % self.grid.height

        print(f"Silver Surfer moves to ({self.x}, {self.y})")

    def attack(self):
        if not self.active:
            return

        cell = self.grid.get_cell(self.x, self.y)
        if cell.cell_type == CellType.BRIDGE:
            bridge = self.grid.get_bridge_at(self.x, self.y)
            if bridge:
                bridge.sabotage()
                self.energy -= 20
                print(f"Silver Surfer sabotages bridge at ({self.x}, {self.y}) - Energy: {self.energy}")

    def avoid_confrontation(self, heroes):
        if not self.active:
            return
        for hero in heroes:
            if hero.x == self.x and hero.y == self.y:
                print("Silver Surfer avoids confrontation and changes path.")
                self.move()

    def withdraw_if_weak(self):
        if self.energy < 20:
            print("Silver Surfer retreats to recover energy.")
            self.active = False

    def persuade_to_retreat(self):
        # Example persuasion mechanic
        if random.random() < 0.3:  # 30% chance persuasion works
            print("Silver Surfer is persuaded to retreat!")
            self.active = False
