import re

def solve_part1(text):
    # Regex pattern
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    # Find all matches
    matches = re.findall(pattern, text)

    # print(matches)  # [('12', '34'), ('456', '789'), ('9', '0')]

    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])
    return result


def solve_part2(text):
    # Not done
    result = 0
    return result


def main():
    # Read input file
    data = []
    data = open("D03/input.txt", "r").readlines()
    text = ''.join(data)

    print(text)

    # Solve and print results
    print("Part 1:", solve_part1(text))
    print("Part 2:", solve_part2(text))


if __name__ == "__main__":
    main()
