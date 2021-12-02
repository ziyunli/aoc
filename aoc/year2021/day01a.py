def gen_nums(f):
    for line in f:
        yield int(line)


def count_increases(nums):

    counter = 0
    prev = -1

    for curr in nums:
        if prev > -1 and prev < curr:
            counter += 1
        prev = curr
    return counter


if __name__ == "__main__":
    f = open("input/2021/day01.txt", "r")

    counter = count_increases(gen_nums(f))
    print(counter)
