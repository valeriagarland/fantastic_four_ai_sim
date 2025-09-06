
from environment.cell import Cell, CellType
from environment.bridge import Bridge
import random

class Grid:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.grid = [[Cell(x, y) for y in range(height)] for x in range(width)]
        self.bridges = []  # Track bridge objects

    def get_cell(self, x, y):
        x %= self.width
        y %= self.height
        return self.grid[x][y]

    def set_cell_type(self, x, y, cell_type):
        cell = self.get_cell(x, y)
        cell.set_type(cell_type)

        # If setting a bridge, create Bridge object
        if cell_type == CellType.BRIDGE:
            bridge = Bridge(x, y)
            self.bridges.append(bridge)

    def get_bridge_at(self, x, y):
        for bridge in self.bridges:
            if bridge.x == x and bridge.y == y:
                return bridge
        return None

    def all_bridges_operational(self):
        return all(bridge.is_complete and not bridge.is_damaged for bridge in self.bridges)

    def display(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row += str(self.grid[x][y]) + " "
            print(row)
        print("\n")

    def random_fill(self):
        # Add some bridges
        for _ in range(5):
            x, y = random.randint(0, self.width-1), random.randint(0, self.height-1)
            self.set_cell_type(x, y, CellType.BRIDGE)
