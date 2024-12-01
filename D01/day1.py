def solve_part1(list1, list2):
    # Example: Sum all integers
    distances = []

    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        distances.append(abs(list1[i] - list2[i]))

    return sum(distances)

def transform_list(li):
  my_dict = {}
  for ID in li:
    if ID in my_dict:
      my_dict[ID] += 1
    else:
      my_dict[ID] = 1

  return my_dict


def solve_part2(list1, list2):
    # Example: Find the first repeated cumulative sum (like a frequency calibration problem)
    list2_to_dict = transform_list(list2)
    # print(list2_to_dict)

    similarities = []

    for ID in list1:
      if ID in list2_to_dict:
        similarities.append(ID * list2_to_dict[ID])


    return sum(similarities)


def main():
    # Read input file
    data = { 'list1': [], 'list2': [] }
    with open("input.txt", "r") as file:
        for line in file.readlines():
          a, b = line.split('   ')
          data['list1'].append(int(a))
          data['list2'].append(int(b))

    # print(data)

    # Solve and print results
    print("Part 1:", solve_part1(data['list1'], data['list2']))
    print("Part 2:", solve_part2(data['list1'], data['list2']))


if __name__ == "__main__":
    main()
