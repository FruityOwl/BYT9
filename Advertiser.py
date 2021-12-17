class Advertiser:
    def __init__(self, adv_id, adv_company, adv_ad_type):
        self.adv_id = adv_id
        self.adv_company = adv_company
        self.adv_ad_type = adv_ad_type

    # Setters

    def set_adv_id(self, adv_id):
        self.adv_id = adv_id

    def set_adv_company(self, adv_company):
        self.adv_company = adv_company

    def set_adv_ad_type(self, adv_ad_type):
        self.adv_ad_type = adv_ad_type

    # Getters

    def get_adv_id(self):
        return self.adv_id

    def get_adv_company(self):
        return self.adv_company

    def get_adv_ad_type(self):
        return self.adv_ad_type

    # Methods

    def provide_ad(self):
        pass
