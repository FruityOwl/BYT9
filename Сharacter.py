import self as self


class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.health_points = 10
        self.char_class = char_class
        self.level = 1

    # Setters
    def set_name(self, name):
        self.name = name

    def set_health_points(self, health_points):
        self.health_points = health_points

    def set_char_class(self, char_class):
        self.char_class = char_class

    def set_level(self, level):
        self.level = level

    # Getters
    def get_name(self):
        return self.name

    def get_health_points(self):
        return self.health_points

    def get_char_class(self):
        return self.char_class

    def get_level(self):
        return self.level

    # Methods
    def level_up(self):
        self.level = self.level + 1

    def info(self):
        print("Name:", self.name, "\nClass:", self.char_class, self.level, "\nHealth points:", self.health_points)
