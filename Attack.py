class Attack:
    def __init__(self, attack_name, attack_damage):
        self.attack_name = attack_name
        self.attack_damage = attack_damage

    # Setters

    def set_attack_name(self, attack_name):
        self.attack_name = attack_name

    def set_attack_damage(self, attack_damage):
        self.attack_damage = attack_damage

    # Getters

    def get_attack_name(self):
        return self.attack_name

    def get_attack_damage(self):
        return self.attack_damage
