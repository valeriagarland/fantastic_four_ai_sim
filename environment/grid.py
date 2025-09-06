
from environment.cell import Cell, CellType
import random

class Grid:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.grid = [
            [Cell(x, y) for y in range(height)] for x in range(width)
        ]

    def get_cell(self, x, y):
        # Wraparound logic
        x %= self.width
        y %= self.height
        return self.grid[x][y]

    def set_cell_type(self, x, y, cell_type):
        cell = self.get_cell(x, y)
        cell.set_type(cell_type)

    def display(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row += str(self.grid[x][y]) + " "
            print(row)
        print("\n")

    def random_fill(self):
        # Fill grid with some example types
        for _ in range(10):
            self.set_cell_type(random.randint(0, self.width-1), random.randint(0, self.height-1), CellType.BRIDGE)
        for _ in range(4):
            self.set_cell_type(random.randint(0, self.width-1), random.randint(0, self.height-1), CellType.HERO)
        self.set_cell_type(random.randint(0, self.width-1), random.randint(0, self.height-1), CellType.SILVER_SURFER)
        self.set_cell_type(random.randint(0, self.width-1), random.randint(0, self.height-1), CellType.GALACTUS)
