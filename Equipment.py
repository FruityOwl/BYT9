class Equipment:
    def __init__(self, eq_id, eq_name, eq_effects, eq_type):
        self.eq_id = eq_id
        self.eq_name = eq_name
        self.eq_effects = eq_effects
        self.eq_type = eq_type

    # Setters

    def set_eq_id(self, eq_id):
        self.eq_id = eq_id

    def set_eq_name(self, eq_name):
        self.eq_name = eq_name

    def set_eq_effects(self, eq_effects):
        self.eq_effects = eq_effects

    def set_eq_type(self, eq_type):
        self.eq_type = eq_type

    # Getters

    def get_eq_id(self):
        return self.eq_id

    def get_eq_name(self):
        return self.eq_name

    def get_eq_effects(self):
        return self.eq_effects

    def get_eq_type(self):
        return self.eq_type
