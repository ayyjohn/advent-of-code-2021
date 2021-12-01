def count_windowed_increases_in_depth():
    depth_increases = 0
    with open("input.txt", "r") as input:
        previous_depth_1 = float("inf")
        previous_depth_2 = float("inf")
        previous_depth_3 = float("inf")
        for line in input.readlines():
            current_depth = int(line)
            previous_window = sum(
                (previous_depth_3, previous_depth_2, previous_depth_1)
            )
            current_window = sum((current_depth, previous_depth_3, previous_depth_2))
            if current_window > previous_window:
                depth_increases += 1
            previous_depth_1 = previous_depth_2
            previous_depth_2 = previous_depth_3
            previous_depth_3 = current_depth
    return depth_increases


if __name__ == "__main__":
    print(count_windowed_increases_in_depth())
