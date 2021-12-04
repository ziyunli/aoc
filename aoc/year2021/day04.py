from typing import List, Tuple


class Board:
    def __init__(self, board: List[List[str]]) -> None:
        self.board = [[int(t) for t in row.split()] for row in board]
        self.drawn = [[False for i in range(5)] for j in range(5)]
        self.unmarked_sum = sum([sum(row) for row in self.board])
        self.winning_draw = None
        self.has_won = False

    def draw(self, num):
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                if num == val:
                    self.drawn[i][j] = True
                    self.unmarked_sum -= num
                    self.has_won = self.check(i, j)
                    if self.has_won:
                        self.winning_draw = num
                        return self.unmarked_sum * num

    def check(self, i, j):
        # Check for row
        row = self.drawn[i]
        full_row = all(row)
        if full_row:
            return full_row
        # Check for col
        col = [self.drawn[i][j] for i in range(5)]
        full_col = all(col)
        if full_col:
            return full_col
        # Default
        return False


def parse(file) -> Tuple[List[int], List[Board]]:
    nums = None
    buffer = []
    boards = []
    for line in file:
        line = line.strip()
        if not line:
            if not buffer:
                continue
            # Create a Bingo board
            board = Board(buffer)
            boards.append(board)
            buffer = []
        elif not nums:
            nums = [int(t) for t in line.split(',')]
        else:
            buffer.append(line)

    if len(buffer) == 5:
        boards.append(Board(buffer))

    return nums, boards


def play(nums, boards):
    for num in nums:
        for board in boards:
            result = board.draw(num)
            if result:
                return board, result


def play_all(nums, boards):
    winners = []
    for num in nums:
        for i, board in enumerate(boards):
            # print(i, board.board, board.has_won)
            if board.has_won:
                continue
            result = board.draw(num)
            if result:
                winners.append((i, result))
    return winners


if __name__ == "__main__":
    with open("input/2021/day04.txt") as reader:
        nums, boards = parse(reader)

        # winner, score = play(nums, boards)
        # print(f"{winner.unmarked_sum} * {winner.winning_draw} = {score}")

        winners = play_all(nums, boards)
        last_winner_idx, score = winners[-1]
        print(f"{boards[last_winner_idx].board}: {score}")
