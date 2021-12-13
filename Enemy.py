class Enemy:
    def __init__(self, enemy_id, enemy_name, enemy_icon, enemy_stats, enemy_attacks, enemy_abilities):
        self.enemy_id = enemy_id
        self.enemy_name = enemy_name
        self.enemy_icon = enemy_icon
        self.enemy_stats = enemy_stats
        self.enemy_attacks = enemy_attacks
        self.enemy_abilities = enemy_abilities

    def enemy_attack(self):
        pass

    def enemy_use_ability(self):
        pass
