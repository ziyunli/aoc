def parse_lanternfishes(file):
    ret = []
    for line in file:
        nums = map(int, line.strip().split(','))
        ret.extend(nums)
    return ret


def step(lanternfishes):
    spawn = []
    for i, fish in enumerate(lanternfishes):
        next_val = fish - 1
        if next_val < 0:
            next_val = 6
            spawn.append(8)
        lanternfishes[i] = next_val
    return lanternfishes + spawn


def run(initial, days):
    curr = initial
    for day in range(days):
        # print(day, curr)
        curr = step(curr)
    return curr


if __name__ == "__main__":
    with open("input/2021/day06.txt") as reader:
        initial = parse_lanternfishes(reader)

        lanternfishes = run(initial, 80)
        print(f"part 1: {lanternfishes} -> {len(lanternfishes)}")
