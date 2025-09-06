# main.py
from environment.grid import Grid
from heroes.reed_richards import ReedRichards
from heroes.ben_grimm import BenGrimm
from entities.silver_surfer import SilverSurfer
from environment.cell import CellType

def main():
    print("Fantastic Four AI Simulation Initialized!\n")

    grid = Grid(20, 20)
    grid.random_fill()
    grid.display()

    # Create heroes
    reed = ReedRichards("Reed", 2, 2, grid)
    ben = BenGrimm("Ben", 5, 5, grid)
    heroes = [reed, ben]

    # Create Silver Surfer (spawn on first bridge for guaranteed sabotage)
    sx, sy = grid.silver_surfer_start
    surfer = SilverSurfer(sx, sy, grid)

    # Simulate turns
    for turn in range(5):
        print(f"\n--- Turn {turn+1} ---")

        # Silver Surfer acts
        surfer.attack()  # sabotage if on a bridge
        surfer.move()
        surfer.avoid_confrontation(heroes)
        surfer.withdraw_if_weak()

        # Heroes act
        for hero in heroes:
            cell = grid.get_cell(hero.x, hero.y)
            if cell.cell_type == CellType.BRIDGE:
                hero.repair_bridge()  # repair if standing on a bridge
            else:
                hero.move(1, 0)  # move right each turn for now
                hero.scan_surroundings()

    # Try persuasion at the end
    surfer.persuade_to_retreat()

    # Final mission status
    print("\n=== Mission Status ===")
    if grid.all_bridges_operational():
        print("All bridges are operational. Earth can teleport safely!")
    else:
        print("Some bridges are still incomplete or damaged! Mission at risk.")

if __name__ == "__main__":
    main()
