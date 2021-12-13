from typing import List, NamedTuple

RAW = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

class Command(NamedTuple ):
    direction: str
    distance: int

    @staticmethod
    def from_string(s):
        direction, distance = s.split()
        return Command(direction, int(distance))


class Position:
    
    def __init__(self, horizontal: int , depth: int):
        self.horizontal = horizontal
        self.depth = depth

    
    def move(self, command: Command):
        if command.direction == 'forward':
            self.horizontal += command.distance
        elif command.direction  == 'up':
            self.depth -= command.distance
        elif command.direction == 'down':
            self.depth += command.distance
        else:
            raise ValueError(f"unkown direction {command.direction}")
        

COMMANDS = [Command.from_string(s) for s in RAW.splitlines()]

POSITION = Position(0,0)
for command in COMMANDS:
    POSITION.move(command)

assert POSITION.horizontal == 15
assert POSITION.depth == 10

class AimPosition:

    def __init__(self, horizontal: int = 0, depth: int= 0, aim: int = 0):
        self.horizontal = horizontal
        self.depth = depth
        self.aim = aim

    
    def move(self, command : Command):
        if command.direction == 'forward':
            self.horizontal += command.distance
            self.depth  += command.distance * self.aim
        elif command.direction == 'up':
            self.aim  -= command.distance
        elif command.direction == 'down':
            self.aim += command.distance
        else:
            raise ValueError(f"unknown direction {command.direction}")
            

if __name__ == '__main__':

    with open("data/day02.txt") as f:
        raw = f.read()
    
    COMMANDS = [Command.from_string(s) for s in raw.splitlines()]

    POSITION = Position(0,0)
    for command in COMMANDS:
        POSITION.move(command)
    
    print(POSITION.depth * POSITION.horizontal)

    AIMPOSITION = AimPosition(0,0)
    for command in COMMANDS:
        AIMPOSITION.move(command)
    
    print(AIMPOSITION.depth * AIMPOSITION.horizontal)





    

