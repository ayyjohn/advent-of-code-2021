def calculate_life_support_rating():
    initial_numbers = []
    with open("input.txt", "r") as input:
        for line in input.readlines():
            number = line.strip()
            initial_numbers.append(number)

    oxy_numbers = initial_numbers[:]
    co2_numbers = initial_numbers[:]

    zero_counts = [0] * 12
    one_counts = [0] * 12
    for i in range(12):
        for number in oxy_numbers:
            if number[i] == "0":
                zero_counts[i] += 1
            elif number[i] == "1":
                one_counts[i] += 1
            else:
                raise Exception("unexpected bit")
        bit_criteria = "0" if zero_counts[i] > one_counts[i] else "1"
        oxy_numbers = [number for number in oxy_numbers if number[i] == bit_criteria]
        if len(oxy_numbers) <= 1:
            break

    zero_counts = [0] * 12
    one_counts = [0] * 12
    for i in range(12):
        for number in co2_numbers:
            if number[i] == "0":
                zero_counts[i] += 1
            elif number[i] == "1":
                one_counts[i] += 1
            else:
                raise Exception("unexpected bit")
        bit_criteria = "1" if zero_counts[i] > one_counts[i] else "0"
        co2_numbers = [number for number in co2_numbers if number[i] == bit_criteria]
        if len(co2_numbers) <= 1:
            break

    oxy_rating, co2_rating = oxy_numbers[0], co2_numbers[0]
    print(oxy_rating, co2_rating)
    print(int(oxy_rating, 2) * int(co2_rating, 2))


if __name__ == "__main__":
    calculate_life_support_rating()
