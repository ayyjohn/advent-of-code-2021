def calculate_position_with_aim():
    x, y, aim = 0, 0, 0
    with open("input.txt", "r") as input:
        for line in input.readlines():
            instruction, value = line.split(" ")
            value = int(value)
            if instruction == "forward":
                x += value
                y += aim * value
            if instruction == "up":
                aim -= value
            if instruction == "down":
                # y is depth, so up decreases
                aim += value

    return x, y


if __name__ == "__main__":
    x, y = calculate_position_with_aim()
    print(x, y)
    # answer is x * y, not x and y
    print(x * y)
