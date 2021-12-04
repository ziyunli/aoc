if __name__ == "__main__":
    with open("input/2021/day03.txt") as reader:
        counts = None
        for line in reader:
            line = line.strip()
            if not counts:
                counts = [{'1': 0, '0': 0} for _ in line]

            for i, ch in enumerate(line):
                counts[i][ch] += 1

        gamma_rate_bits = []
        epsilon_rate_bits = []
        for count in counts:
            if count['0'] > count['1']:
                most_common = '0'
                least_common = '1'
            else:
                most_common = '1'
                least_common = '0'
            gamma_rate_bits.append(most_common)
            epsilon_rate_bits.append(least_common)

        gamma_rate = int(''.join(gamma_rate_bits), 2)
        epsilon_rate = int(''.join(epsilon_rate_bits), 2)

        print(f"part 1: {gamma_rate} * {epsilon_rate} = {gamma_rate * epsilon_rate}")
