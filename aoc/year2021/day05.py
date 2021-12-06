from collections import defaultdict
from dataclasses import dataclass
from typing import List


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


@dataclass(eq=True, frozen=True)
class Segment:
    start: Point
    end: Point

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x

    def is_diagonal(self):
        return abs(self.end.x - self.start.x) == abs(self.end.y - self.start.y)

    def points(self) -> List[Point]:
        if self.is_horizontal():
            step = 1 if self.end.x > self.start.x else -1
            return [Point(x, self.start.y) for x in range(self.start.x, self.end.x + step, step)]
        elif self.is_vertical():
            step = 1 if self.end.y > self.start.y else -1
            return [Point(self.start.x, y) for y in range(self.start.y, self.end.y + step, step)]
        elif self.is_diagonal():
            step_x = 1 if self.end.x > self.start.x else -1
            step_y = 1 if self.end.y > self.start.y else -1
            ret = []
            for n in range(abs(self.end.x - self.start.x) + 1):
                ret.append(Point(self.start.x + step_x * n, self.start.y + step_y * n))
            return ret
        else:
            return []


def parse_segments(file) -> List[Segment]:
    ret = []
    for line in file:
        a, b = line.strip().split('->')
        x1, y1 = map(int, a.strip().split(','))
        start = Point(x=x1, y=y1)
        x2, y2 = map(int, b.strip().split(','))
        end = Point(x=x2, y=y2)
        ret.append(Segment(start, end))
    return ret


if __name__ == "__main__":
    with open("input/2021/day05.txt") as reader:
        segments = parse_segments(reader)

        points = defaultdict(int)
        for segment in segments:
            if segment.is_horizontal() or segment.is_vertical():
                for p in segment.points():
                    points[p] += 1

        count = 0
        for k, v in points.items():
            if v > 1:
                count += 1
        print(f"part 1: {count}")

        points = defaultdict(int)
        for segment in segments:
            for p in segment.points():
                points[p] += 1
        count = 0
        for k, v in points.items():
            if v > 1:
                count += 1
        print(f"part 2: {count}")
