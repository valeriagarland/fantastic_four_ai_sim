# entities/galactus.py
import random
from environment.cell import CellType


class Galactus:
    def __init__(self, x, y, grid, target="bridges", move_interval=1):
        self.x = x
        self.y = y
        self.grid = grid
        self.active = True
        self.turn_counter = 0
        self.move_interval = move_interval
        self.target = target  # "bridges" = random sweep, "franklin" = chase Franklin

    def move(self, franklin_pos=None):
        """Galactus movement depends on difficulty target mode."""
        if not self.active:
            return

        self.turn_counter += 1
        if self.turn_counter % self.move_interval != 0:
            return  # Moves only on scheduled turns

        if self.target == "franklin" and franklin_pos:
            # Hard mode: actively chase Franklin
            fx, fy = franklin_pos
            dx = 1 if fx > self.x else -1 if fx < self.x else 0
            dy = 1 if fy > self.y else -1 if fy < self.y else 0
        else:
            # Easy/Normal: sweeping / random motion
            dx, dy = random.choice([-1, 0, 1]), random.choice([-1, 0, 1])

        # Update position
        self.x = (self.x + dx) % self.grid.width
        self.y = (self.y + dy) % self.grid.height

        # Consume the cell he lands on
        self.consume()

    def consume(self):
        """Consumes the cell at his current location."""
        cell = self.grid.get_cell(self.x, self.y)
        print(f" Galactus consumes {cell.cell_type.name} at ({self.x}, {self.y}).")

        # Track tiles consumed
        self.grid.stats["galactus_consumed"] = self.grid.stats.get("galactus_consumed", 0) + 1

        # If it’s a bridge, mark it destroyed
        if cell.cell_type == CellType.BRIDGE:
            bridge = self.grid.get_bridge_at(self.x, self.y)
            if bridge:
                bridge.sabotage()
                self.grid.stats["galactus_sabotages"] = self.grid.stats.get("galactus_sabotages", 0) + 1

        # Mark space as "E" = empty
        cell.set_type(CellType.EMPTY)

    def check_franklin(self, franklin_pos):
        """Check if Galactus has reached Franklin (game over)."""
        if (self.x, self.y) == franklin_pos:
            print("Galactus reaches Franklin Richards and consumes him!")
            return True
        return False
