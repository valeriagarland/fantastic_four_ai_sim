from heroes.hero_base import HeroBase

class ReedRichards(HeroBase):
    def use_ability(self):
        print(f"{self.name} predicts threat movements and optimizes pathfinding.")
        # Track ability usage
        self.grid.stats["reed_abilities"] = self.grid.stats.get("reed_abilities", 0) + 1

    def take_turn(self, franklin_pos, surfer):
        self.scan_surroundings()

        # Recharge if low on energy
        if self.energy < 20:
            target = self.find_nearest_recharge()
            if target:
                self.move_towards(*target)
                return

        # Deliver components to bridges
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
            # Patrol Franklin if no bridges need repair
            fx, fy = franklin_pos
            self.move_towards(fx, fy)
            print(f"{self.name} patrols near Franklin.")
