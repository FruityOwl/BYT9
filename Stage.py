class Stage:
    def __init__(self, floor_number, rooms, boss):
        self.floor_number = floor_number
        self.rooms = rooms
        self.boss = boss

    # Setters

    def set_floor_number(self, floor_number):
        self.floor_number = floor_number

    def set_rooms(self, rooms):
        self.rooms = rooms

    def set_boss(self, boss):
        self.boss = boss

    # Getters

    def get_floor_number(self):
        return self.floor_number

    def get_rooms(self):
        return self.rooms

    def get_boss(self):
        return self.boss
