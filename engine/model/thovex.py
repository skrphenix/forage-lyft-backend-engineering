from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Thovex(CapuletEngine):
    def needs_service(self) -> bool:
        ...
