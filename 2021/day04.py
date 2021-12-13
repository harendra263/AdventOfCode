from typing import List

RAW = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


class Board:

    def __init__(self,grid: List[List[str]]):
        self.grid = grid
        self.nr = len(grid)
        self.nc = len(grid[0])

        self.row_counts = [0 for _ in range(self.nr)]
        self.col_counts = [0 for _ in range(self.nc)]


    
    def mark(self, number: int) -> None:
        for i in range(self.nr):
            for j in range(self.nc):
                if self.grid[i][j] == number:
                    self.row_counts[i] += 1
                    self.col_counts[j] += 1
                    self.grid[i][j] = -1
    
    def is_winner(self) -> bool:
        if any(rc == self.nc for rc in self.row_counts):
            return True
        if any(cc == self.nr for cc in self.col_counts):
            return True
        else:
            return False
    
    def score(self, number: int) -> int:
        """Return the score of the board"""
        return number * sum(entry
                            for row in self.grid
                            for entry in row
                            if entry != -1)

    @staticmethod
    def parse(raw: str) -> 'Board':
        grid = [
            [int(n) for n in row.split()]
            for row in raw.split('\n')
        ]


class Game:
    def __init__(self, numbers: List[int], boards: List[Board]) -> None:
        self.numbers = numbers
        self.boards = boards
    
    def play(self) -> int:
        """Play the game and return the final score of the winning board"""
        for number in self.numbers:
            for board in self.boards:
                pass

    


