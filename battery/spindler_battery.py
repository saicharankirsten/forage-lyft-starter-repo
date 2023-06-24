from battery import battery

class spindler_battery(battery):

    def __init__(self,last_service_date,current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if (self.cuurent_data - self.last_service_date) == 2:
            return True
        else:
            return False