from heroes.hero_base import HeroBase

class SueStorm(HeroBase):
    def use_ability(self):
        print(f"{self.name} generates an invisible shield to protect nearby allies.")
        # Track ability usage
        self.grid.stats["sue_abilities"] = self.grid.stats.get("sue_abilities", 0) + 1

    def take_turn(self, franklin_pos, surfer):
        # Recharge if needed
        if self.energy < 20:
            target = self.find_nearest_recharge()
            if target:
                self.move_towards(*target)
                return

        # Help with bridges if needed
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
            # Default: protect Franklin
            fx, fy = franklin_pos
            self.move_towards(fx, fy)
            self.use_ability()
