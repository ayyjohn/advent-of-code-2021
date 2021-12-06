class BingoBoard:
    def __init__(self, grid):
        self.grid = grid
        self.numbers = set()
        self.locations = {}
        for x, row in enumerate(self.grid):
            for y, number in enumerate(row):
                self.numbers.add(number)
                self.locations[number] = (x, y)
        self.called = []
        self.completed = False

    def call(self, number):
        if number in self.numbers:
            self.called.append(number)
            x, y = self.locations[number]
            self[x, y] = "x"

    def complete(self):
        if self.completed:
            return True
        self.completed = self.complete_horizontally() or self.complete_vertically()
        return self.completed

    def complete_horizontally(self):
        for row in self.rows():
            if all(x == "x" for x in row):
                return True
        return False

    def complete_vertically(self):
        for column in self.columns():
            if all(x == "x" for x in column):
                return True
        return False

    def current_total(self):
        return sum(i for row in self.rows() for i in row if i != "x")

    def columns(self):
        for i in range(5):
            yield [self[j, i] for j in range(5)]

    def rows(self):
        for row in self.grid:
            yield row

    def __getitem__(self, position):
        row, col = position
        return self.grid[row][col]

    def __setitem__(self, position, value):
        row, col = position
        self.grid[row][col] = value

    def __str__(self):
        return (
            "\n"
            + "Bingo Board:\n"
            + "\n".join(" ".join(map(str, row)) for row in self.grid)
            + "\n"
        )


def play_bingo(numbers_to_call, bingo_boards):
    incomplete_boards = len(bingo_boards)
    complete_boards = set()
    for number in numbers_to_call:
        print(f"calling {number}")
        print()
        for index, board in enumerate(bingo_boards):
            board.call(number)
            print(index, board)
            if board.complete():
                if index not in complete_boards:
                    incomplete_boards -= 1
                complete_boards.add(index)
                if incomplete_boards == 0:
                    # last board to finish
                    ct = board.current_total()
                    print(ct)
                    print(number)
                    print(number * ct)
                    return


def calculate_winning_bingo_score():
    # assemble boards and parse input
    with open("day_4/input.txt", "r") as input:
        lines = input.readlines()
    # first line is numbers
    numbers_to_call = list(map(int, lines[0].strip().split(",")))
    # print(numbers_to_call)

    bingo_boards = []
    current_board = []
    for line in map(str.strip, lines[2:]):
        if line == "":
            # I added a final newline to the input
            # so that this catches the last one
            # print("empty line")
            bingo_boards.append(BingoBoard(current_board))
            current_board = []
        else:
            # numbers can be one digit so de-pad by replacing double spaces with a single space
            current_line = list(map(int, line.replace("  ", " ").split(" ")))
            # print(current_line)
            current_board.append(current_line)

    # play the game
    play_bingo(numbers_to_call, bingo_boards)


if __name__ == "__main__":
    calculate_winning_bingo_score()
