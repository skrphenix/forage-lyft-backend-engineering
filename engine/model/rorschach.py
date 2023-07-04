from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Rorschach(WilloughbyEngine):
    def needs_service(self) -> bool:
        ...
