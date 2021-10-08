from typing import NamedTuple
import re

rgx = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"

class Rectangle:
    id: int
    x_lo: int
    y_lo: int
    x_hi: int
    y_hi: int

    @staticmethod
    def from_claim(claim: str) -> 'Rectangle':
        id ,x_lo,y_lo, width, height = re.match(rgx, claim).groups()
        return Rectangle(id, x_lo, y_lo, x_lo + width, y_lo + height)


assert Rectangle.from_claim("#123 @ 3,2: 5x4") == \
     Rectangle(123,3, 2,8, 6)


