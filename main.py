# main.py
import random
from environment.grid import Grid
from heroes.reed_richards import ReedRichards
from heroes.ben_grimm import BenGrimm
from heroes.johnny_storm import JohnnyStorm
from heroes.sue_storm import SueStorm
from entities.silver_surfer import SilverSurfer
from entities.galactus import Galactus


def main():
    print(" Fantastic Four AI Simulation Initialized!\n")

    # === Ask for difficulty ===
    difficulty = input("Select difficulty (easy / normal / hard): ").strip().lower()
    if difficulty not in ["easy", "normal", "hard"]:
        print("Invalid choice! Defaulting to 'normal'.")
        difficulty = "normal"

    # === Configure settings based on difficulty ===
    settings = {
        "easy": {
            "bridges": 3,
            "components": 2,
            "recharge_zones": 4,
            "galactus_speed": 2,
            "surfer_aggression": 0.3,
            "bridge_completion_ratio": 0.6,
        },
        "normal": {
            "bridges": 5,
            "components": 3,
            "recharge_zones": 3,
            "galactus_speed": 1,
            "surfer_aggression": 0.5,
            "bridge_completion_ratio": 0.75,
        },
        "hard": {
            "bridges": 7,
            "components": 4,
            "recharge_zones": 2,
            "galactus_speed": 1,
            "surfer_aggression": 0.8,
            "bridge_completion_ratio": 1.0,
        },
    }
    config = settings[difficulty]

    # === Create grid with difficulty config ===
    grid = Grid(20, 20, config)
    grid.stats = {}  # <-- track hero/surfer/galactus stats
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
    mission_failed = False
    failure_reason = ""

    for turn in range(1, MAX_TURNS + 1):
        print(f"\n=== Turn {turn} ===")

        # Introduce Silver Surfer at Turn 3
        if turn == 3 and surfer is None:
            sx, sy = grid.bridges[0].x, grid.bridges[0].y
            surfer = SilverSurfer(sx, sy, grid, aggression=config["surfer_aggression"])
            print(f" Silver Surfer appears at {sx},{sy}!")

        # Introduce Galactus at Turn 6
        if turn == 6 and galactus is None:
            # Hard mode: Galactus targets Franklin directly
            target_mode = "franklin" if difficulty == "hard" else "bridges"
            galactus = Galactus(0, 0, grid, target=target_mode, move_interval=config["galactus_speed"])
            print(" Galactus projection emerges in the sky!")

        # Silver Surfer actions
        if surfer and surfer.active:
            surfer.attack()
            surfer.move()
            surfer.avoid_confrontation(heroes)
            surfer.withdraw_if_weak()

        # Galactus actions
        if galactus and galactus.active:
            galactus.move(franklin_pos)
            if galactus.check_franklin(franklin_pos):
                mission_failed = True
                failure_reason = "Franklin Richards was consumed by Galactus!"
                break

        # Hero actions
        for hero in heroes:
            hero.take_turn(franklin_pos, surfer)

        # Check win condition early
        operational = sum(1 for b in grid.bridges if b.is_complete and not b.is_damaged)
        total = len(grid.bridges)
        if operational / total >= config["bridge_completion_ratio"] and galactus is None:
            print("\n  Mission Accomplished Early: Enough bridges complete before Galactus arrives!")
            return

    # Persuade Surfer at the end (difficulty scaling handled inside class)
    if surfer:
        surfer.persuade_to_retreat(difficulty)

    # === Final Mission Report ===
    print("\n=== Final Mission Report ===")
    print(f"Mode: {difficulty.capitalize()}")

    operational = sum(1 for b in grid.bridges if b.is_complete and not b.is_damaged)
    total = len(grid.bridges)

    if mission_failed:
        print(f" Status: Mission Failed \nReason: {failure_reason}")
    elif operational / total >= config["bridge_completion_ratio"]:
        print(" Status: Mission Success \nReason: Enough bridges operational. Earth teleports safely!")
    else:
        print(" Status: Mission Failed \nReason: Some bridges were incomplete or destroyed.")

    # === Extra Hero & Threat Statistics ===
    print("\n--- Mission Statistics ---")
    print(f"Reed’s strategic plans: {grid.stats.get('reed_abilities', 0)}")
    print(f"Sue’s shields: {grid.stats.get('sue_abilities', 0)}")
    print(f"Johnny’s fire attacks: {grid.stats.get('johnny_attacks', 0)}")
    print(f"Ben’s brute strength uses: {grid.stats.get('ben_strength', 0)}")
    print(f"Silver Surfer sabotages: {grid.stats.get('surfer_sabotages', 0)}")
    print(f"Galactus consumptions: {grid.stats.get('galactus_consumed', 0)}")


if __name__ == "__main__":
    main()
