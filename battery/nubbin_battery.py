from datetime import date

from battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        self.last_service_date: date = last_service_date
        self.current_date: date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < self.current_date
