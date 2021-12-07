from collections import defaultdict
from copy import copy

if False:  # TYPE_CHECKCING
    from typing import DefaultDict, List


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


def gen_states(fishes: List[int]) -> DefaultDict[int, int]:
    states = defaultdict(int)
    for fish in fishes:
        states[fish] += 1

    return states


def step_states(states: DefaultDict[int, int]) -> DefaultDict[int, int]:
    new_states = defaultdict(int)
    for state, count in states.items():
        if state == 0:
            new_states[6] += count  # Parents
            new_states[8] += count  # Children
        else:
            new_states[state - 1] += count
    return new_states


def run_states(initial: DefaultDict[int, int], days: int) -> DefaultDict[int, int]:
    curr = initial
    for day in range(days):
        curr = step_states(curr)
    return curr


if __name__ == "__main__":
    with open("input/2021/day06.txt") as reader:
        initial = parse_lanternfishes(reader)

        lanternfishes = run(copy(initial), 80)
        print(f"part 1: {len(lanternfishes)}")

        initial_states = gen_states(copy(initial))
        final_states = run_states(initial_states, 256)
        print(f"part 2: {sum(final_states.values())}")
