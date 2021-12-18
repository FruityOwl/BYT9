class Weapon:
    def __init__(self, weapon_dice, weapon_type):
        self.weapon_dice = weapon_dice
        self.weapon_type = weapon_type

    # Setters
    def set_weapon_dice(self, weapon_dmg_dice):
        self.weapon_dice = weapon_dmg_dice

    def set_weapon_type(self, weapon_type):
        self.weapon_type = weapon_type

    # Getters

    def get_weapon_dice(self):
        return self.weapon_dice

    def get_weapon_type(self):
        return self.weapon_type
