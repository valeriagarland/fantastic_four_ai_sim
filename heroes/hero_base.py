
from abc import ABC, abstractmethod
from environment.cell import CellType

class HeroBase(ABC):
    def __init__(self, name, x, y, grid, energy=100):
        self.name = name
        self.x = x
        self.y = y
        self.grid = grid
        self.energy = energy
        self.max_energy = 100

    def move(self, dx, dy):
        if self.energy <= 0:
            print(f"{self.name} has no energy to move.")
            return

        self.x = (self.x + dx) % self.grid.width
        self.y = (self.y + dy) % self.grid.height
        self.energy -= 5  # Cost of moving

        print(f"{self.name} moved to ({self.x}, {self.y}) - Energy: {self.energy}")

    def scan_surroundings(self, radius=1):
        print(f"{self.name} scans surroundings:")
        for dx in range(-radius, radius + 1):
            for dy in range(-radius, radius + 1):
                cx = (self.x + dx) % self.grid.width
                cy = (self.y + dy) % self.grid.height
                cell = self.grid.get_cell(cx, cy)
                print(f"  ({cx},{cy}) -> {cell.cell_type.name}")

    def repair_bridge(self):
        cell = self.grid.get_cell(self.x, self.y)
        if cell.cell_type == CellType.BRIDGE:
            print(f"{self.name} repairs bridge at ({self.x}, {self.y})")
            self.energy -= 10
        else:
            print(f"{self.name} is not on a bridge cell.")

    def recharge(self):
        print(f"{self.name} is recharging...")
        self.energy = self.max_energy

    def share_energy(self, other_hero, amount):
        if self.energy >= amount:
            self.energy -= amount
            other_hero.energy = min(other_hero.energy + amount, other_hero.max_energy)
            print(f"{self.name} shares {amount} energy with {other_hero.name}")

    @abstractmethod
    def use_ability(self):
        pass
