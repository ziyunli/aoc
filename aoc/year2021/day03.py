from typing import Dict, List


def parse_report(file) -> List[str]:
    values = []
    for line in file:
        values.append(line.strip())
    return values


def bit_counts(values: List[str]) -> List[Dict[str, int]]:
    counts = None
    for val in values:
        if not counts:
            counts = [{'1': 0, '0': 0} for _ in val]
        for i, ch in enumerate(val):
            counts[i][ch] += 1

    return counts


def most_common_bits(counts: List[Dict[str, int]]) -> List[str]:
    ret = []
    for count in counts:
        if count['0'] > count['1']:
            most_common = '0'
        else:
            most_common = '1'
        ret.append(most_common)
    return ret


def least_common_bits(counts: List[Dict[str, int]]) -> List[str]:
    ret = []
    for count in counts:
        if count['0'] > count['1']:
            least_common = '1'
        else:
            least_common = '0'
        ret.append(least_common)
    return ret


def find_rating(values: List[str], most_common):
    if not values:
        return None

    curr_list = values
    width = len(values[0])

    for i in range(width):
        count_0 = 0
        count_1 = 0
        next_list = []
        for val in curr_list:
            if val[i] == '0':
                count_0 += 1
            else:
                count_1 += 1

        if most_common:
            bit = '1' if count_1 >= count_0 else '0'
        else:
            bit = '0' if count_0 <= count_1 else '1'

        for val in curr_list:
            if val[i] == bit:
                next_list.append(val)
        if len(next_list) == 1:
            return next_list[0]
        curr_list = next_list

    return None


if __name__ == "__main__":
    with open("input/2021/day03.txt") as reader:
        values = parse_report(reader)
        counts = bit_counts(values)

        gamma_rate_bits = most_common_bits(counts)
        epsilon_rate_bits = least_common_bits(counts)

        gamma_rate = int(''.join(gamma_rate_bits), 2)
        epsilon_rate = int(''.join(epsilon_rate_bits), 2)

        print(f"part 1: {gamma_rate} * {epsilon_rate} = {gamma_rate * epsilon_rate}")

        oxygen_generator_rating = int(find_rating(values, True), 2)
        co2_scrubber_rating = int(find_rating(values, False), 2)
        print(
            f"part 2: {oxygen_generator_rating} * {co2_scrubber_rating} \
                = {oxygen_generator_rating * co2_scrubber_rating}"
        )
