from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        # super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date