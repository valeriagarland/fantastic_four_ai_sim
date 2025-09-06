
from environment.cell import CellType

class Galactus:
    def __init__(self, x, y, grid, target="bridges"):
        self.x = x
        self.y = y
        self.grid = grid
        self.active = True
        self.target = target  # "bridges" or "franklin"
        self.direction = (1, 0)  # moves right by default (can make smarter later)

    def move(self):
        if not self.active:
            return

        dx, dy = self.direction
        self.x = (self.x + dx) % self.grid.width
        self.y = (self.y + dy) % self.grid.height

        print(f" Galactus projection moves to ({self.x}, {self.y})")
        self.consume()

    def consume(self):
        cell = self.grid.get_cell(self.x, self.y)

        if cell.cell_type == CellType.BRIDGE:
            bridge = self.grid.get_bridge_at(self.x, self.y)
            if bridge:
                print(f" Galactus destroys bridge at ({self.x}, {self.y})!")
                bridge.is_damaged = True
                bridge.is_complete = False

        elif cell.cell_type == CellType.HERO:
            print(f" Galactus consumes a hero at ({self.x}, {self.y})!")

        elif cell.cell_type == CellType.EMPTY:
            print(f"Galactus consumes empty space at ({self.x}, {self.y}).")

        elif cell.cell_type == CellType.SILVER_SURFER:
            print("⚡ Galactus ignores Silver Surfer (herald).")

        elif cell.cell_type == CellType.GALACTUS:
            pass  # already projection

    def check_franklin(self, franklin_pos):
        if (self.x, self.y) == franklin_pos:
            print(" Galactus has reached Franklin Richards! Mission failed!")
            self.active = False
            return True
        return False
