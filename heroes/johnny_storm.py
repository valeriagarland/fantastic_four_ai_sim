from heroes.hero_base import HeroBase

class JohnnyStorm(HeroBase):
    def use_ability(self):
        if self.energy >= 15:
            self.energy -= 15
            print(f"{self.name} launches a ranged fire attack! Energy left: {self.energy}")
            # Track ability usage
            self.grid.stats["johnny_attacks"] = self.grid.stats.get("johnny_attacks", 0) + 1
        else:
            print(f"{self.name} doesn't have enough energy to use fire attack.")

    def take_turn(self, franklin_pos, surfer):
        # Recharge if low
        if self.energy < 20:
            target = self.find_nearest_recharge()
            if target:
                self.move_towards(*target)
                return

        # Hunt Silver Surfer if active
        if surfer and surfer.active:
            self.move_towards(surfer.x, surfer.y)
            self.use_ability()
        else:
            # Patrol Franklin if no Surfer threat
            fx, fy = franklin_pos
            self.move_towards(fx, fy)
            print(f"{self.name} patrols near Franklin.")
