from typing import List

from tires import Tires

_T = List[float]


class CarriganTires(Tires):
    def __init__(self, tire_wear: _T):
        self.tire_wear: _T = tire_wear

    def needs_service(self):
        return max(self.tire_wear) >= 0.9
