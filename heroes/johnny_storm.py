
from heroes.hero_base import HeroBase

class JohnnyStorm(HeroBase):
    def use_ability(self):
        if self.energy >= 15:
            self.energy -= 15
            print(f"{self.name} launches a ranged fire attack! Energy left: {self.energy}")
        else:
            print(f"{self.name} doesn't have enough energy to use fire attack.")
