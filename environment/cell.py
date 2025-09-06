from enum import Enum, auto

class CellType(Enum):
    EMPTY = auto()
    BRIDGE = auto()
    HERO = auto()
    SILVER_SURFER = auto()
    GALACTUS = auto()
    RECHARGE = auto()  # recharge zone

class Cell:
    def __init__(self, x, y, cell_type=CellType.EMPTY):
        self.x = x
        self.y = y
        self.cell_type = cell_type

    def __str__(self):
        return f"{self.cell_type.name[0]}"

    def set_type(self, new_type):
        self.cell_type = new_type
