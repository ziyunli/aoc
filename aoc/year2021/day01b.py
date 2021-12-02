from collections import deque


def gen_nums(f):
    for line in f:
        yield int(line)


def count_increases(nums):
    window = deque()
    counter = 0

    for curr in nums:
        if len(window) == 3:
            first = window.popleft()
            if curr > first:
                counter += 1
        window.append(curr)
    return counter


if __name__ == "__main__":
    f = open("input/2021/day01.txt", "r")

    counter = count_increases(gen_nums(f))
    print(counter)
