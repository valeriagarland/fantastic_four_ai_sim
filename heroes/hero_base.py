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
        self.carrying_component = False  # 🔹 transport system

    def move(self, dx, dy):
        if self.energy <= 0:
            print(f"{self.name} has no energy to move.")
            return

        self.x = (self.x + dx) % self.grid.width
        self.y = (self.y + dy) % self.grid.height
        self.energy -= 5  # Cost of moving

        print(f"{self.name} moved to ({self.x}, {self.y}) - Energy: {self.energy}")

        # Check if on recharge zone
        cell = self.grid.get_cell(self.x, self.y)
        if cell.cell_type == CellType.RECHARGE:
            self.recharge()

    def scan_surroundings(self, radius=1):
        print(f"{self.name} scans surroundings:")
        for dx in range(-radius, radius + 1):
            for dy in range(-radius, radius + 1):
                cx = (self.x + dx) % self.grid.width
                cy = (self.y + dy) % self.grid.height
                cell = self.grid.get_cell(cx, cy)
                print(f"  ({cx},{cy}) -> {cell.cell_type.name}")

    def repair_bridge(self):
        """Deliver component to a bridge if carrying one."""
        cell = self.grid.get_cell(self.x, self.y)
        if cell.cell_type == CellType.BRIDGE:
            bridge = self.grid.get_bridge_at(self.x, self.y)
            if bridge:
                if self.carrying_component:
                    bridge.deliver_component(self)  # 🔹 use multi-delivery system
                    self.energy -= 10
                else:
                    print(f"{self.name} is on a bridge but has no component.")
        else:
            print(f"{self.name} is not on a bridge cell.")

    def pick_up_component(self):
        """Pick up a component if not already carrying one."""
        if not self.carrying_component:
            self.carrying_component = True
            print(f"{self.name} picks up a component.")
        else:
            print(f"{self.name} is already carrying a component.")

    def recharge(self):
        """Recharge hero’s energy at recharge zones."""
        old_energy = self.energy
        self.energy = min(self.max_energy, self.energy + 30)  # recharge faster
        print(f"{self.name} recharges at ({self.x},{self.y}) - Energy: {old_energy} → {self.energy}")

    def share_energy(self, other_hero, amount=10):
        """Share energy with nearby allies if possible."""
        if self.energy >= amount and abs(self.x - other_hero.x) <= 1 and abs(self.y - other_hero.y) <= 1:
            self.energy -= amount
            other_hero.energy = min(other_hero.energy + amount, other_hero.max_energy)
            print(f"{self.name} shares {amount} energy with {other_hero.name}")
        else:
            print(f"{self.name} cannot share energy with {other_hero.name} (too far or low energy).")

    @abstractmethod
    def use_ability(self):
        pass

    def find_nearest_bridge(self):
        """Find the closest bridge that is incomplete or damaged."""
        nearest = None
        min_dist = float("inf")

        for bridge in self.grid.bridges:
            if not bridge.is_complete or bridge.is_damaged:
                dist = abs(bridge.x - self.x) + abs(bridge.y - self.y)
                if dist < min_dist:
                    min_dist = dist
                    nearest = bridge

        return nearest

    def find_nearest_recharge(self):
        """Locate nearest recharge zone."""
        nearest = None
        min_dist = float("inf")

        for x in range(self.grid.width):
            for y in range(self.grid.height):
                cell = self.grid.get_cell(x, y)
                if cell.cell_type == CellType.RECHARGE:
                    dist = abs(x - self.x) + abs(y - self.y)
                    if dist < min_dist:
                        min_dist = dist
                        nearest = (x, y)

        return nearest

    def move_towards(self, target_x, target_y):
        """Take one step toward target coordinates."""
        if self.energy <= 0:
            print(f"{self.name} has no energy to move.")
            return

        dx, dy = 0, 0
        if target_x > self.x:
            dx = 1
        elif target_x < self.x:
            dx = -1
        if target_y > self.y:
            dy = 1
        elif target_y < self.y:
            dy = -1

        self.move(dx, dy)
