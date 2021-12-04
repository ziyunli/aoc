from collections import namedtuple
from typing import List

from .command import Command, Direction

Position = namedtuple("Position", ['x', 'y'])


def parse_commands(file):
    ret = []
    for line in file:
        x, y = line.strip().split()

        cmd = Command(direction=Direction(x.upper()), step=int(y))
        ret.append(cmd)
    return ret


def move(pos: Position, cmd: Command) -> Position:
    match cmd.direction:
        case Direction.FORWARD:
            return Position(x=pos.x + cmd.step, y=pos.y)
        case Direction.BACKWARD:
            return Position(x=pos.x - cmd.step, y=pos.y)
        case Direction.UP:
            return Position(x=pos.x, y=pos.y - cmd.step)
        case Direction.DOWN:
            return Position(x=pos.x, y=pos.y + cmd.step)


def move_submarine(start: Position, commands: List[Command]) -> Position:
    curr = start
    for cmd in commands:
        curr = move(curr, cmd)
    return curr


if __name__ == "__main__":
    with open("input/2021/day02.txt") as reader:
        commands = parse_commands(reader)
        print(commands)
        final = move_submarine(Position(x=0, y=0), commands)

        print(final.x * final.y)
