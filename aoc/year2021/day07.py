from statistics import median_high


def parse_numbers(file):
    ret = []
    for line in file:
        nums = map(int, line.strip().split(','))
        ret.extend(nums)
    return ret


def calculate_fuels(positions):
    median = median_high(positions)

    s = 0
    for pos in positions:
        s += abs(pos - median)

    return s


if __name__ == "__main__":
    with open("input/2021/day07.txt") as reader:
        nums = parse_numbers(reader)

        print(f"part 1: {calculate_fuels(nums)}")
