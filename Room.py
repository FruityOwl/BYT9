class Room:
    def __init__(self, room_id, room_type, room_reward):
        self.room_id = room_id
        self.room_type = room_type
        self.room_reward = room_reward

    # Setters

    def set_room_id(self, room_id):
        self.room_id = room_id

    def set_room_type(self, room_type):
        self.room_type = room_type

    def set_room_reward(self, room_reward):
        self.room_reward = room_reward

    # Getters

    def get_room_id(self):
        return self.room_id

    def get_room_type(self):
        return self.room_type

    def get_room_reward(self):
        return self.room_reward

    # Methods

    def give_reward(self, char):
        pass
