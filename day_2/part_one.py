def calculate_position():
    x, y = 0, 0
    with open("input.txt", "r") as input:
        for line in input.readlines():
            direction, value = line.split(" ")
            value = int(value)
            if direction == "forward":
                x += value
            if direction == "up":
                # y is depth, so up decreases
                y -= value
            if direction == "down":
                # y is depth, so up decreases
                y += value
    return x, y


if __name__ == "__main__":
    x, y = calculate_position()
    print(x, y)
    # answer is x * y, not x and y
    print(x * y)
