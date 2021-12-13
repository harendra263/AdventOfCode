from typing import List

RAW = """1721
979
366
299
675
1456"""

INPUT = [int(i) for i in RAW.splitlines()]

def find_product(numbers: List[int]) -> int:
    """
    Find the two elements that add up to 2020
    and return their product
    """
    needs = {2020 - i for i in numbers}

    for i in numbers:
        if i in needs:
            return i*(2020-i)


assert find_product(INPUT) == 514579

def find_product3(numbers: List[int]) -> int:
    """
    Find the three elements that add up to 2020
    and return their product
    """
    needs = {2020 - i - j: (i, j)
            for i in numbers
            for j in numbers if i != j}

    for i in numbers:
        if i in needs:
            j, k = needs[i]
            return i * j * k


if __name__ == "__main__":

   numbers = [int(i) for i in open('data/day01.txt').read().splitlines()]

   print(find_product(numbers))
   print(find_product3(numbers))



