
class Bridge:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_complete = False
        self.is_damaged = False

    def sabotage(self):
        if not self.is_complete:
            print(f"Bridge at ({self.x}, {self.y}) is sabotaged before completion!")
        else:
            print(f"Bridge at ({self.x}, {self.y}) has been damaged!")
        self.is_damaged = True
        self.is_complete = False

    def repair(self):
        if self.is_damaged or not self.is_complete:
            self.is_damaged = False
            self.is_complete = True
            print(f"Bridge at ({self.x}, {self.y}) has been repaired and is now operational!")
        else:
            print(f"Bridge at ({self.x}, {self.y}) is already operational.")

    def status(self):
        if self.is_complete:
            return "Operational"
        elif self.is_damaged:
            return "Damaged"
        else:
            return "Incomplete"
