import self as self


class Character:
    def __init__(self, char_name, char_stats, char_class):
        self.char_name = char_name
        self.char_stats = char_stats
        self.health_points = 10
        self.char_ac = 10 + char_stats.get_dex_modifier()
        self.char_class = char_class
        self.level = 1

    # Setters

    def set_name(self, char_name):
        self.char_name = char_name

    def set_health_points(self, health_points):
        self.health_points = health_points

    def set_char_class(self, char_class):
        self.char_class = char_class

    def set_level(self, level):
        self.level = level

    def set_char_ac(self, char_ac):
        self.char_ac = char_ac

    def set_char_stats(self, char_stats):
        self.char_stats = char_stats

    # Getters

    def get_name(self):
        return self.char_name

    def get_health_points(self):
        return self.health_points

    def get_char_class(self):
        return self.char_class

    def get_level(self):
        return self.level

    def get_char_ac(self):
        return self.char_ac

    def get_char_stats(self):
        return self.char_stats

    # Methods

    def level_up(self):
        self.level = self.level + 1

    def info(self):
        print("Name:", self.char_name, "\nClass:", self.char_class, self.level, "\nHealth points:", self.health_points)

    def char_damage(self, damage):
        self.health_points = self.get_health_points() - damage
