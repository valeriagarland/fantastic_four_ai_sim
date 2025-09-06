import random

class Bridge:
    def __init__(self, x, y, required_components=None):
        self.x = x
        self.y = y
        # Each bridge needs 2–4 components unless overridden by config
        self.required_components = required_components if required_components else random.randint(2, 4)
        self.delivered_components = 0
        self.is_complete = False
        self.is_damaged = False

    def sabotage(self):
        if not self.is_complete:
            print(f" Bridge at ({self.x}, {self.y}) is sabotaged before completion!")
        else:
            print(f" Bridge at ({self.x}, {self.y}) has been damaged!")
        self.is_damaged = True
        self.is_complete = False

    def deliver_component(self, hero):
        """Heroes deliver components until the bridge is operational."""
        if self.is_complete:
            print(f"Bridge at ({self.x}, {self.y}) is already operational.")
            return

        self.delivered_components += 1
        hero.carrying_component = False
        print(f"{hero.name} delivered a component at ({self.x},{self.y}). "
              f"Progress: {self.delivered_components}/{self.required_components}")

        if self.delivered_components >= self.required_components:
            self.is_complete = True
            self.is_damaged = False
            print(f"  Bridge at ({self.x}, {self.y}) is now operational!")

    def repair(self):
        """Fallback repair if a bridge is sabotaged after being completed."""
        if self.is_damaged:
            self.is_damaged = False
            self.is_complete = True
            print(f"Bridge at ({self.x}, {self.y}) has been repaired and is now operational!")
        elif not self.is_complete:
            print(f"Bridge at ({self.x}, {self.y}) is incomplete. Needs {self.required_components} components.")
        else:
            print(f"Bridge at ({self.x}, {self.y}) is already operational.")

    def status(self):
        if self.is_complete:
            return "Operational"
        elif self.is_damaged:
            return "Damaged"
        else:
            return f"Incomplete ({self.delivered_components}/{self.required_components})"
