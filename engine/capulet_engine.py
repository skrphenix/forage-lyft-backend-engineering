from engine import Engine


class CapuletEngine(Engine):
    def __init__(
        self,
        last_service_mileage: int,
        current_mileage: int,
    ) -> None:
        self.last_service_mileage: int = last_service_mileage
        self.current_mileage: int = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000
