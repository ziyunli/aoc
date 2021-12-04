from collections import namedtuple
from dataclasses import dataclass
from enum import Enum, auto
from typing import List


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class Direction(AutoName):
    FORWARD = auto()
    BACKWARD = auto()
    UP = auto()
    DOWN = auto()


Command = namedtuple("Command", ['direction', 'step'])


@dataclass
class Position:
    x: int
    y: int

    def move(self, cmd):
        match cmd.direction:
            case Direction.FORWARD:
                return Position(x=self.x + cmd.step, y=self.y)
            case Direction.BACKWARD:
                return Position(x=self.x - cmd.step, y=self.y)
            case Direction.UP:
                return Position(x=self.x, y=self.y - cmd.step)
            case Direction.DOWN:
                return Position(x=self.x, y=self.y + cmd.step)


@dataclass
class Status:
    pos: Position
    aim: int

    def move(self, cmd):
        match cmd.direction:
            case Direction.FORWARD:
                pos = Position(x=self.pos.x + cmd.step, y=self.pos.y + self.aim * cmd.step)
                return Status(pos=pos, aim=self.aim)
            case Direction.UP:
                return Status(pos=self.pos, aim=self.aim - cmd.step)
            case Direction.DOWN:
                return Status(pos=self.pos, aim=self.aim + cmd.step)
            case _:
                return None


def parse_commands(file):
    ret = []
    for line in file:
        x, y = line.strip().split()

        cmd = Command(direction=Direction(x.upper()), step=int(y))
        ret.append(cmd)
    return ret


def move_submarine(start: (Position | Status), commands: List[Command]) -> (Position | Status):
    curr = start
    for cmd in commands:
        curr = curr.move(cmd)
    return curr


if __name__ == "__main__":
    with open("input/2021/day02.txt") as reader:
        commands = parse_commands(reader)

        sol_1 = move_submarine(Position(x=0, y=0), commands)
        print("part 1: ", sol_1.x * sol_1.y)

        sol_2 = move_submarine(Status(Position(0, 0), 0), commands)
        print("part 2: ", sol_2.pos.x * sol_2.pos.y)
