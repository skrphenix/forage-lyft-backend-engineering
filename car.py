# Interfaces
from serviceable import Serviceable
from engine import Engine
from battery import Battery
from tires import Tires


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tires: Tires):
        self.engine: Engine = engine
        self.battery: Battery = battery
        self.tires: Tires = tires

    def needs_service(self) -> bool:
        return any([
            self.engine.needs_service(), self.battery.needs_service(),
            self.tires.needs_service()
        ])
