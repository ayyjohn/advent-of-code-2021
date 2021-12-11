def calculate_lanternfish_count():
    with open("day_6/input.txt", "r") as input:
        initial_state = list(map(int, input.read().strip().split(",")))

    cache = {}
    cache_hits = [0]

    def num_fish(days, days_remaining):
        total = 1
        for i in range(days):
            if days_remaining == 0:
                days_remaining = 7
                if (days - i, 9) in cache:
                    cache_hits[0] += 1
                    total += cache[(days - i, 9)]
                else:
                    new_fish = num_fish(days - i, 9)
                    cache[(days - i, 9)] = new_fish
                    total += new_fish
            days_remaining -= 1
        return total

    total_fish = 0
    for days_remaining in initial_state:
        total_fish += num_fish(256, days_remaining)

    print(total_fish)
    print(cache_hits)


if __name__ == "__main__":
    calculate_lanternfish_count()
