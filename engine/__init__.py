from abc import ABC, abstractmethod

from . import model


class Engine(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
