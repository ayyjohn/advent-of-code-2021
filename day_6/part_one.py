def calculate_lanternfish_count():
    with open("day_6/example.txt", "r") as input:
        initial_state = list(map(int, input.read().strip().split(",")))

    fishes = initial_state[:]
    for i in range(18):
        for index, days in enumerate(fishes):
            if days == 0:
                fishes[index] = 6
                fishes.append(9)
            else:
                fishes[index] -= 1
    print(len(fishes))


if __name__ == "__main__":
    calculate_lanternfish_count()
