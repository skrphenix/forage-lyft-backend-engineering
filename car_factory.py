from datetime import date
from typing import Union, List

# Car
from car import Car

# Engine
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

# Battery
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

# Tires
from tires import Tires


class CarFactory:
    @staticmethod
    def create_calliope(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int,
        tires: Tires
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)

        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_glissade(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int,
        tires: Tires
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)

        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_palindrome(
        current_date: date, last_service_date: date,
        warning_light_on: bool, tires: Tires
    ) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)

        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_rorschach(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int,
        tires: Tires
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)

        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_thovex(
        current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int,
        tires: Tires
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)

        car = Car(engine, battery, tires)
        return car
