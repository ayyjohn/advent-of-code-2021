def calculate_power_consumption():
    zero_counts = [0] * 12
    one_counts = [0] * 12
    with open("input.txt", "r") as input:
        for line in input.readlines():
            number = line.strip()
            for index, bit in enumerate(number):
                if bit == "0":
                    zero_counts[index] += 1
                elif bit == "1":
                    one_counts[index] += 1
                else:
                    raise Exception("unexpected bit")

    print(zero_counts)
    print(one_counts)
    gamma_rate = ""
    epsilon_rate = ""
    for zero_count, one_count in zip(zero_counts, one_counts):
        if zero_count > one_count:
            gamma_rate += "0"
            epsilon_rate += "1"
        elif one_count > zero_count:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            raise Exception("counts equal")

    print(f"gamma rate: {gamma_rate}, epsilon_rate: {epsilon_rate}")
    print(f"power consumption: {int(gamma_rate, 2) * int(epsilon_rate, 2)}")


if __name__ == "__main__":
    calculate_power_consumption()
