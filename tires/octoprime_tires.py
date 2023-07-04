from typing import List

from tires import Tires

_T = List[float]


class OctoprimeTires(Tires):
    def __init__(self, tire_wear: _T):
        self.tire_wear: _T = tire_wear

    def needs_service(self):
        return sum(self.tire_wear) >= 3.0
