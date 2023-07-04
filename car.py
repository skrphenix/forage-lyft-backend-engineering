from datetime import date

from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()


class CarFactory:
    @staticmethod
    def create_calliope(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int
    ) -> Car:
        ...

    @staticmethod
    def create_glissade(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int
    ) -> Car:
        ...

    @staticmethod
    def create_palindrome(
        current_date: date, last_service_date: date,
        warning_light_on: bool
    ) -> Car:
        ...

    @staticmethod
    def create_rorschach(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int
    ) -> Car:
        ...

    @staticmethod
    def create_thovex(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int
    ) -> Car:
        ...
