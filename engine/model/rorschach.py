from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine

from battery.spindler_battery import SpindlerBattery


class Rorschach(WilloughbyEngine, SpindlerBattery):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, current_mileage, last_service_mileage)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
