from environment.cell import Cell, CellType
from environment.bridge import Bridge
import random


class Grid:
    def __init__(self, width=20, height=20, config=None):
        self.width = width
        self.height = height
        self.grid = [[Cell(x, y) for y in range(height)] for x in range(width)]
        self.bridges = []         # Track bridge objects
        self.recharge_zones = []  # Track recharge locations
        self.config = config if config else {
            "bridges": 5,
            "components": 3,
            "recharge_zones": 3
        }

    def get_cell(self, x, y):
        x %= self.width
        y %= self.height
        return self.grid[x][y]

    def set_cell_type(self, x, y, cell_type):
        cell = self.get_cell(x, y)
        cell.set_type(cell_type)

        # If setting a bridge, create Bridge object with required components from config
        if cell_type == CellType.BRIDGE:
            bridge = Bridge(x, y, required_components=self.config.get("components", 3))
            self.bridges.append(bridge)

        # If setting recharge zone, track it
        if cell_type == CellType.RECHARGE:
            self.recharge_zones.append((x, y))

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
        # Add bridges based on difficulty config
        for _ in range(self.config.get("bridges", 5)):
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            self.set_cell_type(x, y, CellType.BRIDGE)

        # Add recharge zones based on difficulty config
        for _ in range(self.config.get("recharge_zones", 3)):
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            self.set_cell_type(x, y, CellType.RECHARGE)

        # Place Silver Surfer initially on the first bridge (if exists)
        if self.bridges:
            bx, by = self.bridges[0].x, self.bridges[0].y
            self.set_cell_type(bx, by, CellType.SILVER_SURFER)
            self.silver_surfer_start = (bx, by)
        else:
            # fallback in case no bridge exists
            sx, sy = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            self.set_cell_type(sx, sy, CellType.SILVER_SURFER)
            self.silver_surfer_start = (sx, sy)
