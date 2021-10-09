from typing import NamedTuple, Iterator, Tuple, Dict, List
import re
from collections import Counter

rgx = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"

Coord = Tuple[int, int]

class Rectangle(NamedTuple):
    id: int
    x_lo: int
    y_lo: int
    x_hi: int
    y_hi: int

    @staticmethod
    def from_claim(claim: str) -> "Rectangle":
        id ,x_lo,y_lo, width, height = [int(x) for x in re.match(rgx, claim).groups()]
        return Rectangle(id, x_lo, y_lo, x_lo + width, y_lo + height)

    
    def all_squares(self) -> Iterator[Coord]:
        for i in range(self.x_lo, self.x_hi):
            for j in range(self.y_lo, self.y_hi):
                yield(i, j)



# assert Rectangle.from_claim("#123 @ 3,2: 5x4") == Rectangle(123,3, 2,8, 6)
# print(Rectangle.all_squares("#123 @ 3,2: 5x4"))

def coverage(rectangles: List[Rectangle]) -> Dict[Coord, int]:
    counts = Counter()
    for rectangle in rectangles:
        for coord in rectangle.all_squares():
            counts[coord]  += 1
    
    return counts


def multi_claimed(claims: List[str]) -> int:
    rectangles = [Rectangle.from_claim(claim) for claim in claims]
    counts = coverage(rectangles)
    return len([count for count in counts.values() if count>=2])


with open("data/day03.txt") as f:
    claims = [line.strip() for line in f]


print(multi_claimed(claims))



