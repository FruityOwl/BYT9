# Stats are just like from D&D, so 12 means +1 to this stat 8 means -1 and so on

class Stats:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    # Setters

    def set_strength(self, strength):
        self.strength = strength

    def set_dexterity(self, dexterity):
        self.dexterity = dexterity

    def set_constitution(self, constitution):
        self.constitution = constitution

    def set_intelligence(self, intelligence):
        self.intelligence = intelligence

    def set_wisdom(self, wisdom):
        self.wisdom = wisdom

    def set_charisma(self, charisma):
        self.charisma = charisma

    # Getters

    def get_strength(self):
        return self.strength

    def get_dexterity(self):
        return self.dexterity

    def get_constitution(self):
        return self.constitution

    def get_intelligence(self):
        return self.intelligence

    def get_wisdom(self):
        return self.wisdom

    def get_charisma(self):
        return self.charisma

    # Methods

    # All modifiers would be necessary in rolls and other stuff
    def get_str_modifier(self):
        return (self.strength - 10) / 2

    def get_dex_modifier(self):
        return (self.dexterity - 10) / 2

    def get_con_modifier(self):
        return (self.constitution - 10) / 2

    def get_int_modifier(self):
        return (self.intelligence - 10) / 2

    def get_wis_modifier(self):
        return (self.wisdom - 10) / 2

    def get_cha_modifier(self):
        return (self.charisma - 10) / 2
