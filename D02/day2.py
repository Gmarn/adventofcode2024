def safe_line(line):
    first_result = line[0] - line[1]
    if (first_result == 0 or abs(first_result) > 3):
        return False

    increasing = bool(first_result > 0)

    for level_id in range(1, len(line)):
        dif = line[level_id - 1] - line[level_id]
        if dif == 0:
            return False
        elif abs(dif) > 3:
            return False
        elif bool(dif > 0) != increasing:
            return False
    return True

def solve_part1(data):
    safe_lines_count = 0
    for line in data:
        print(line, "Result: ", safe_line(line))
        if safe_line(line):
            safe_lines_count += 1

    return safe_lines_count


def solve_part2(data):
    # Not done
    return "IN Progress"


def main():
    # Read input file
    data = []
    with open("test_input.txt", "r") as file:
        for line in file.readlines():
            line_with_number = []
            for number in line.split(' '):
                line_with_number.append(int(number))
            data.append(line_with_number)

    print(data)

    # Solve and print results
    print("Part 1:", solve_part1(data))
    # print("Part 2:", solve_part2(data))


if __name__ == "__main__":
    main()
