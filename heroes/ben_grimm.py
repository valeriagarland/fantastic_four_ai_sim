
from heroes.hero_base import HeroBase

class BenGrimm(HeroBase):
    def use_ability(self):
        if self.energy >= 10:
            self.energy -= 10
            print(f"{self.name} uses brute strength for repairs or melee combat. Energy left: {self.energy}")
        else:
            print(f"{self.name} is too tired to use his strength.")
