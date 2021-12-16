class Enemy:
    def __init__(self, enemy_id, enemy_name, enemy_type, enemy_icon, enemy_stats, enemy_attacks, enemy_abilities):
        self.enemy_id = enemy_id
        self.enemy_name = enemy_name
        self.enemy_type = enemy_type
        self.enemy_icon = enemy_icon
        self.enemy_stats = enemy_stats
        self.enemy_attacks = enemy_attacks
        self.enemy_abilities = enemy_abilities

    # Setters
    def set_enemy_id(self, enemy_id):
        self.enemy_id = enemy_id

    def set_enemy_name(self, enemy_name):
        self.enemy_name = enemy_name

    def set_enemy_type(self, enemy_type):
        self.enemy_type = enemy_type

    def set_enemy_icon(self, enemy_icon):
        self.enemy_icon = enemy_icon

    def set_enemy_stats(self, enemy_stats):
        self.enemy_stats = enemy_stats

    def set_enemy_attacks(self, enemy_attacks):
        self.enemy_attacks = enemy_attacks

    def set_enemy_abilities(self, enemy_abilities):
        self.enemy_abilities = enemy_abilities

    # Getters
    def get_enemy_id(self):
        return self.enemy_id

    def get_enemy_name(self):
        return self.enemy_name

    def get_enemy_type(self):
        return self.enemy_type

    def get_enemy_icon(self):
        return self.enemy_icon

    def get_enemy_stats(self):
        return self.enemy_stats

    def get_enemy_attacks(self):
        return self.enemy_attacks

    def get_enemy_abilities(self):
        return self.enemy_abilities

    # Methods
    def enemy_attack(self):
        pass

    def enemy_use_ability(self):
        pass
