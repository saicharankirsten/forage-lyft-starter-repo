from datetime import datetime

from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery


class Palindrome(SternmanEngine, SpindlerBattery):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date, warning_light_is_on)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
