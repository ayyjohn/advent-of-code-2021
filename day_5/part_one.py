def map_vents():
    # create the initial grid
    # iterate through each line and
    # fill the board
    board = [[0] * 1000 for i in range(1000)]
    with open("day_5/input.txt", "r") as input:
        for line in input.readlines():
            print(line)
            point1, point2 = line.split(" -> ")
            x1, y1 = map(int, point1.split(","))
            x2, y2 = map(int, point2.split(","))
            # print(x1, y1)
            # print(x2, y2)
            if x1 == x2:
                print("vertical line")
                x = x1
                # convert lines that are backward
                if y2 < y1:
                    y2, y1 = y1, y2
                # +1s are because lines are inclusive
                for y in range(y1, y2 + 1):
                    board[y][x] += 1
            elif y1 == y2:
                print("horizontal line")
                y = y1
                if x2 < x1:
                    x2, x1 = x1, x2
                for x in range(x1, x2 + 1):
                    board[y][x] += 1
            else:
                print("nonvertical line")
                # raise Exception("not a horizontal or vertical line")
            # for line in board:
            #     print(line)
            # print()
    print()
    dangerous_points = 0
    for line in board:
        dangerous_points += sum([1 for x in line if x > 1])
        print(line)
    print(dangerous_points)


if __name__ == "__main__":
    map_vents()
