class User:
    
    def __init__(self,chat_id):
        self.chat_id = chat_id
        self.periodicity = ""

        self.gadget_type = ""
        self.gadget_focus = 0
        
        self.time_zone = 0
        self.latitude = 0
        self.country = ""
        self.city = ""

    def set_periodicity(self, periodicity):
        self.periodicity = periodicity

    def set_gadget_type(self, gadget_type):
        self.gadget_type = gadget_type

    def set_gadget_focus(self, gadget_focus):
        self.gadget_focus = gadget_focus

    def set_time_zone(self, time_zone):
        self.time_zone = time_zone

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    
