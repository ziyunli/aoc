from collections import namedtuple
from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class Direction(AutoName):
    FORWARD = auto()
    BACKWARD = auto()
    UP = auto()
    DOWN = auto()


Command = namedtuple("Command", ['direction', 'step'])
