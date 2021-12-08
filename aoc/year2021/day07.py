from statistics import median_high


def parse_numbers(file):
    ret = []
    for line in file:
        nums = map(int, line.strip().split(','))
        ret.extend(nums)
    return ret


def calculate_fuels(positions):
    final_position = median_high(nums)
    s = 0
    for pos in positions:
        s += abs(pos - final_position)

    return s


# def calculate_crab_fuels(positions):
#     final_position = int(round(mean(nums)))

#     s = 0
#     for pos in positions:
#         diff = abs(pos - final_position)
#         fuel = int(diff * (diff + 1) / 2)
#         s += fuel
#     return s


def calculate_crab_fuels(positions):
    final_position = None
    total_fuels = None
    min_position = min(positions)
    max_position = max(positions)
    for i in range(min_position, max_position + 1):
        fuels = 0
        for pos in positions:
            diff = abs(i - pos)
            fuel = int(diff * (diff + 1) / 2)
            fuels += fuel
        if not total_fuels or total_fuels > fuels:
            final_position = pos
            total_fuels = fuels
    return final_position, total_fuels


if __name__ == "__main__":
    with open("input/2021/day07.txt") as reader:
        nums = parse_numbers(reader)

        print(f"part 1: {calculate_fuels(nums)}")

        print(f"part 2: {calculate_crab_fuels(nums)}")
