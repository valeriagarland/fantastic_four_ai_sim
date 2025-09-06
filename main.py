# main.py
import random
from environment.grid import Grid
from heroes.reed_richards import ReedRichards
from heroes.ben_grimm import BenGrimm
from heroes.johnny_storm import JohnnyStorm
from heroes.sue_storm import SueStorm
from entities.silver_surfer import SilverSurfer
from entities.galactus import Galactus
from environment.cell import CellType

def main():
    print(" Fantastic Four AI Simulation Initialized!\n")

    # Create grid
    grid = Grid(20, 20)
    grid.random_fill()
    grid.display()

    # Place Franklin Richards (center of grid)
    franklin_pos = (grid.width // 2, grid.height // 2)
    print(f" Franklin Richards is at {franklin_pos}\n")

    # Create heroes
    reed = ReedRichards("Reed", 2, 2, grid)
    sue = SueStorm("Sue", 3, 3, grid)
    johnny = JohnnyStorm("Johnny", 4, 4, grid)
    ben = BenGrimm("Ben", 5, 5, grid)
    heroes = [reed, sue, johnny, ben]

    # Threats (added later in timeline)
    surfer = None
    galactus = None

    MAX_TURNS = 15
    for turn in range(1, MAX_TURNS + 1):
        print(f"\n=== Turn {turn} ===")

        # Introduce Silver Surfer at Turn 3
        if turn == 3 and surfer is None:
            sx, sy = grid.bridges[0].x, grid.bridges[0].y
            surfer = SilverSurfer(sx, sy, grid)
            print(f"⚡ Silver Surfer appears at {sx},{sy}!")

        # Introduce Galactus at Turn 6
        if turn == 6 and galactus is None:
            galactus = Galactus(0, 0, grid, target="bridges")
            print(" Galactus projection emerges in the sky!")

        # Silver Surfer actions
        if surfer and surfer.active:
            surfer.attack()
            surfer.move()
            surfer.avoid_confrontation(heroes)
            surfer.withdraw_if_weak()

        # Galactus actions
        if galactus and galactus.active:
            galactus.move()
            if galactus.check_franklin(franklin_pos):
                print(" Mission failed: Franklin consumed!")
                return

        # Hero actions
        for hero in heroes:
            cell = grid.get_cell(hero.x, hero.y)
            if cell.cell_type == CellType.BRIDGE:
                hero.repair_bridge()
            else:
                # Random wandering for now
                hero.move(random.choice([-1, 0, 1]), random.choice([-1, 0, 1]))
                hero.scan_surroundings()

        # Check win condition early
        if grid.all_bridges_operational() and galactus is None:
            print("\n Mission success: All bridges complete before Galactus arrives!")
            return

    # Persuade Surfer at the end
    if surfer:
        surfer.persuade_to_retreat()

    # Final mission status
    print("\n=== Final Mission Status ===")
    if grid.all_bridges_operational():
        print(" All bridges are operational. Earth teleports safely!")
    else:
        print(" Some bridges are incomplete or destroyed. Mission at risk!")

if __name__ == "__main__":
    main()
