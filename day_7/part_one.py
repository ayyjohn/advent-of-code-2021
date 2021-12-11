from statistics import mean


def calculate_fuel_usage():
    with open("day_7/example.txt", "r") as input:
        initial_positions = list(map(int, input.read().strip().split(",")))
        print(initial_positions)
        min_position = min(initial_positions)
        max_position = max(initial_positions)
        print(min_position, max_position)
        min_fuel_used = float("inf")
        output_position = None
        for destination_position in range(min_position, max_position):
            fuel_used = sum(
                abs(position - destination_position) for position in initial_positions
            )
            if fuel_used < min_fuel_used:
                output_position = destination_position
                min_fuel_used = fuel_used
            print(destination_position, fuel_used)
        print()
        print(output_position, min_fuel_used)


if __name__ == "__main__":
    calculate_fuel_usage()
