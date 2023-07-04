from engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: bool):
        self.warning_light_is_on: bool = warning_light_is_on

    def needs_service(self) -> bool:
        return self.warning_light_is_on
