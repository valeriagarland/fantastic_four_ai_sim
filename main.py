# main.py
from environment.grid import Grid
from heroes.reed_richards import ReedRichards
from heroes.ben_grimm import BenGrimm
from entities.silver_surfer import SilverSurfer
from entities.galactus import Galactus
from environment.cell import CellType

def main():
    print("Fantastic Four AI Simulation Initialized!\n")

    grid = Grid(20, 20)
    grid.random_fill()
    grid.display()

    # Place Franklin Richards (center of the grid)
    franklin_pos = (grid.width // 2, grid.height // 2)
    print(f"Franklin Richards is at {franklin_pos}")

    # Create heroes
    reed = ReedRichards("Reed", 2, 2, grid)
    ben = BenGrimm("Ben", 5, 5, grid)
    heroes = [reed, ben]

    # Create Silver Surfer (spawned from grid)
    sx, sy = grid.silver_surfer_start
    surfer = SilverSurfer(sx, sy, grid)

    # Create Galactus projection
    galactus = Galactus(0, 0, grid, target="bridges")

    # Simulate turns
    for turn in range(8):
        print(f"\n--- Turn {turn+1} ---")

        # Silver Surfer
        surfer.attack()
        surfer.move()
        surfer.avoid_confrontation(heroes)
        surfer.withdraw_if_weak()

        # Galactus
        galactus.move()
        if galactus.check_franklin(franklin_pos):
            print(" Mission failed: Franklin consumed!")
            return

        # Heroes
        for hero in heroes:
            cell = grid.get_cell(hero.x, hero.y)
            if cell.cell_type == CellType.BRIDGE:
                hero.repair_bridge()
            else:
                hero.move(1, 0)
                hero.scan_surroundings()

    # Persuade Surfer at the end
    surfer.persuade_to_retreat()

    # Final mission status
    print("\n=== Mission Status ===")
    if grid.all_bridges_operational():
        print(" All bridges are operational. Earth can teleport safely!")
    else:
        print(" Some bridges are still incomplete or damaged! Mission at risk.")

if __name__ == "__main__":
    main()
