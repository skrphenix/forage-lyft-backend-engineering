from datetime import date

from serviceable import Serviceable
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


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
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_glissade(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(
        current_date: date, last_service_date: date,
        warning_light_on: bool
    ) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
