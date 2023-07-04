from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    def needs_service(self) -> bool:
        ...
