# main.py
from environment.grid import Grid
from heroes.reed_richards import ReedRichards
from heroes.ben_grimm import BenGrimm

def main():
    print("Fantastic Four AI Simulation Initialized!\n")

    grid = Grid(20, 20)
    grid.random_fill()
    grid.display()

    # Place heroes
    reed = ReedRichards("Reed", 2, 2, grid)
    ben = BenGrimm("Ben", 5, 5, grid)

    # Force Ben onto a bridge for testing
    if grid.bridges:
        bx, by = grid.bridges[0].x, grid.bridges[0].y
        ben.x, ben.y = bx, by
        print(f"{ben.name} starts at bridge ({bx}, {by})")

        # Simulate sabotage
        bridge = grid.get_bridge_at(bx, by)
        bridge.sabotage()

        # Ben repairs it
        ben.repair_bridge()

    # Check mission status
    if grid.all_bridges_operational():
        print("All bridges are operational. Earth can teleport safely!")
    else:
        print("Some bridges are still incomplete or damaged!")

if __name__ == "__main__":
    main()
