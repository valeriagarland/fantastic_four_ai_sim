import random
from environment.cell import CellType

class SilverSurfer:
    def __init__(self, x, y, grid, aggression=0.5):
        self.x = x
        self.y = y
        self.grid = grid
        self.energy = 100
        self.active = True
        self.aggression = aggression  # difficulty-based aggression level

    def move(self):
        """Moves around the grid. Aggressive Surfer targets bridges."""
        if not self.active:
            return

        # Energy cost for moving
        self.energy -= 2
        if self.energy <= 0:
            self.withdraw_if_weak()
            return

        if random.random() < self.aggression and self.grid.bridges:
            # Aggressively seek a random bridge
            bridge = random.choice(self.grid.bridges)
            dx = 1 if bridge.x > self.x else -1 if bridge.x < self.x else 0
            dy = 1 if bridge.y > self.y else -1 if bridge.y < self.y else 0
        else:
            # Random roaming
            dx, dy = random.choice([-1, 0, 1]), random.choice([-1, 0, 1])

        self.x = (self.x + dx) % self.grid.width
        self.y = (self.y + dy) % self.grid.height
        print(f"Silver Surfer moves to ({self.x}, {self.y}) - Energy: {self.energy}")

    def attack(self):
        """Attacks bridges when standing on one."""
        if not self.active:
            return

        if self.energy <= 0:
            self.withdraw_if_weak()
            return

        cell = self.grid.get_cell(self.x, self.y)
        if cell.cell_type == CellType.BRIDGE:
            bridge = self.grid.get_bridge_at(self.x, self.y)
            if bridge:
                bridge.sabotage()
                self.energy -= 10
                print(f"Silver Surfer sabotages bridge at ({self.x},{self.y}). Energy left: {self.energy}")
                # Track sabotage
                self.grid.stats["surfer_sabotages"] = self.grid.stats.get("surfer_sabotages", 0) + 1

    def avoid_confrontation(self, heroes):
        """Surfer avoids heroes if too close."""
        if not self.active:
            return

        for hero in heroes:
            if abs(hero.x - self.x) <= 1 and abs(hero.y - self.y) <= 1:
                print("Silver Surfer avoids confrontation and changes path.")
                self.energy -= 5
                self.x = (self.x + random.choice([-1, 1])) % self.grid.width
                self.y = (self.y + random.choice([-1, 1])) % self.grid.height

    def withdraw_if_weak(self):
        """Withdraws if energy < 20%."""
        if self.energy < 20:
            self.active = False
            print("Silver Surfer withdraws due to low energy!")
            # Track retreat
            self.grid.stats["surfer_retreats"] = self.grid.stats.get("surfer_retreats", 0) + 1

    def persuade_to_retreat(self, difficulty):
        """Difficulty-based persuasion at the end of the mission."""
        if not self.active:
            return

        chances = {"easy": 0.7, "normal": 0.4, "hard": 0.1}
        retreat_chance = chances.get(difficulty, 0.4)

        if random.random() < retreat_chance:
            self.active = False
            print("Silver Surfer is persuaded to retreat!")
            self.grid.stats["surfer_retreats"] = self.grid.stats.get("surfer_retreats", 0) + 1
        else:
            print("Silver Surfer refuses to retreat.")
