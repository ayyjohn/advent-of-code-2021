def count_increases_in_depth():
    depth_increases = 0
    with open("input.txt", "r") as input:
        previous_depth = float("inf")
        for line in input.readlines():
            depth = int(line)
            if depth > previous_depth:
                depth_increases += 1
            previous_depth = depth
    return depth_increases


if __name__ == "__main__":
    print(count_increases_in_depth())
