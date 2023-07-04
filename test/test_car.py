import unittest
from datetime import date

from car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class TestCarService(unittest.TestCase):
    def test_car_should_be_serviced(self):
        engine = CapuletEngine(0, 25_000)

        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 10)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_car_should_not_be_serviced(self):
        engine = CapuletEngine(0, 25_000)

        current_date = date.today()
        last_service_date = current_date.replace(current_date.year - 1)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
