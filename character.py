import self as self


class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.health_points = 10
        self.char_class = char_class
        self.level = 1

    def level_up(self):
        self.level = self.level + 1

    def info(self):
        print("Name:", self.name, "\nClass:", self.char_class, self.level, "\nHealth points:", self.health_points)
