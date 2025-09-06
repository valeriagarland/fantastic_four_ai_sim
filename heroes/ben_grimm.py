from heroes.hero_base import HeroBase

class BenGrimm(HeroBase):
    def use_ability(self):
        if self.energy >= 10:
            self.energy -= 10
            print(f"{self.name} uses brute strength for repairs or melee combat. Energy left: {self.energy}")
            # Track ability usage
            self.grid.stats["ben_strength"] = self.grid.stats.get("ben_strength", 0) + 1
        else:
            print(f"{self.name} is too tired to use his strength.")

    def take_turn(self, franklin_pos, surfer):
        # Recharge if low
        if self.energy < 20:
            target = self.find_nearest_recharge()
            if target:
                self.move_towards(*target)
                return

        # Prioritize bridge repairs
        target_bridge = self.find_nearest_bridge()
        if target_bridge:
            if self.x == target_bridge.x and self.y == target_bridge.y:
                if not self.carrying_component:
                    self.pick_up_component()
                target_bridge.deliver_component(self)
                self.use_ability()
            else:
                self.move_towards(target_bridge.x, target_bridge.y)
        else:
            # Patrol Franklin if no bridges left
            fx, fy = franklin_pos
            self.move_towards(fx, fy)
            print(f"{self.name} patrols near Franklin.")
