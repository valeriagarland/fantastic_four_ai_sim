# main.py
from environment.grid import Grid

def main():
    print("Fantastic Four AI Simulation Initialized!\n")

    grid = Grid(20, 20)
    grid.random_fill()
    grid.display()

if __name__ == "__main__":
    main()
