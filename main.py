# main.py
from environment.grid import Grid
from heroes.reed_richards import ReedRichards
from heroes.sue_storm import SueStorm
from heroes.johnny_storm import JohnnyStorm
from heroes.ben_grimm import BenGrimm

def main():
    print("Fantastic Four AI Simulation Initialized!\n")

    grid = Grid(20, 20)
    grid.random_fill()
    grid.display()

    # Create heroes
    reed = ReedRichards("Reed", 2, 2, grid)
    sue = SueStorm("Sue", 3, 3, grid)
    johnny = JohnnyStorm("Johnny", 4, 4, grid)
    ben = BenGrimm("Ben", 5, 5, grid)

    # Example hero actions
    reed.scan_surroundings()
    reed.move(1, 0)
    reed.use_ability()

    sue.move(0, 1)
    sue.use_ability()

    ben.repair_bridge()
    johnny.use_ability()

if __name__ == "__main__":
    main()
