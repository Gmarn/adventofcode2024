def check(line):
    count = 0
    if "".join(line[3:7]) == 'XMAS':
        count += 1
    if "".join(line[0:4]) == 'SAMX':
        count += 1
    return count

def check_a_position_1(data):
    count = 0

    column = [line[3] for line in data]
    diagonal_1 = [data[i][i] for i in range(0, 7)]
    diagonal_2 = [data[6-i][i] for i in range(0, 7)]

    count += check(data[3])
    count += check(column)
    count += check(diagonal_1)
    count += check(diagonal_2)

    return count

def select_portion(data, x, size):
    for y in range(0,len(data)):
        data[y] = data[y][x-size:x+size+1]
    # for line in select_portion(data[y-3:y+4], x):
    #     print("".join(line))
    # print(' ')

    return data

def solve_part1(data):
    count = 0
    # y is a line position
    # x is a column position
    for y in range(3, len(data) - 3):
        for x in range(3, len(data[y]) - 3):
            point = data[y][x]
            if point != 'X':
                continue
            else:
                count += check_a_position_1(select_portion(data[y-3:y+4], x, 3))

    return count

def check_x(data):
    count = 0

    diagonal_1 = [data[i][i] for i in range(0, 3)]
    diagonal_2 = [data[2-i][i] for i in range(0, 3)]

    if "M" in diagonal_1 and "S" in diagonal_1 and "M" in diagonal_2 and "S" in diagonal_2:
        count += 1

    return count

def solve_part2(data):
    count = 0
    for y in range(3, len(data) - 3):
        for x in range(3, len(data[y]) - 3):
            point = data[y][x]
            if point != 'A':
                continue
            else:
                count += check_x(select_portion(data[y-1:y+2], x, 1))

    return count

def add_border_to(data):
    dot_list = ['.'] * len(data[0])
    data = [dot_list] + [dot_list] + [dot_list] + data + [dot_list] + [dot_list] + [dot_list]

    for y in range(0,len(data)):
        data[y] = ['.'] + ['.'] + ['.'] + data[y] + ['.'] + ['.'] + ['.']
    return data

def main():
    # Read input file
    data = []
    with open("D04/input.txt", "r") as file:
        for line in file.readlines():
            data.append(list(line.strip()))

    data = add_border_to(data)
    # print(data)

    for line in data:
        print("".join(line))
    # Solve and print results
    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))


if __name__ == "__main__":
    main()
