neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
squares = [(0, 0), (0, 1), (1, 1), (1, 0) ,(0, 2), (1, 2), (2, 2), (2, 1), (2, 0)]
diagonals = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

small_square = [(0,0), (0,1), (1,1), (1,0)]

def compute_sides(borders):
    sides = 0
    min_x, max_x = min([border[0] for border in borders]), max([border[0] for border in borders])
    min_y, max_y = min([border[1] for border in borders]), max([border[1] for border in borders])

    for i in range(min_x - 1, max_x + 2):
        for j in range(min_y - 1, max_y + 2):
            count_borders = 0
            for square in small_square:
                if (i + square[0], j + square[1]) in borders:
                    count_borders += 1
            if count_borders == 3:
                sides += 1
    return sides

def print_borders(borders, corners = {}):
    min_x, max_x = min([border[0] for border in borders]), max([border[0] for border in borders])
    min_y, max_y = min([border[1] for border in borders]), max([border[1] for border in borders])
    print()
    for i in range(min_x - 1, max_x + 2):
        for j in range(min_y - 1, max_y + 2):
            if (i, j) in borders:
                print('#', end='')
            elif (i, j) in corners and corners[(i, j)] != 0:
                print(corners[(i, j)], end='')
            else:
                print('.', end='')
        print()


def extend_region(region, borders):
    min_x, max_x = min([element[0] for element in region]), max([element[0] for element in region])
    min_y, max_y = min([element[1] for element in region]), max([element[1] for element in region])
    new_region = []
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if (i, j) in region:
                for square in squares:
                    new_region.append((i * 3 + square[0], j * 3 + square[1]))
    new_borders = []
    for element in new_region:
        for neighbour in neighbours:
            if (element[0] + neighbour[0], element[1] + neighbour[1]) not in new_region:
                new_borders.append((element[0] + neighbour[0], element[1] + neighbour[1]))

    for element in new_region:
        for diagonal in diagonals:
            if (element[0] + diagonal[0], element[1] + diagonal[1]) not in new_borders and (element[0] + diagonal[0], element[1] + diagonal[1]) not in new_region:
                new_borders.append((element[0] + diagonal[0], element[1] + diagonal[1]))

    return compute_sides(new_borders)


def compute(content, part=1):
    dict = {}
    for i, line in enumerate(content):
        for j, element in enumerate(line.rstrip()):
            dict[(i, j)] = element

    groups = []
    for key in dict:
        if dict[key] != 1:
            region = [key]
            nexts = [key]
            borders = []
            while len(nexts) > 0:
                next_nexts = []
                for next in nexts:
                    for neighbour in neighbours:
                        new_key = (next[0] + neighbour[0], next[1] + neighbour[1])
                        if new_key in dict and new_key not in region and dict[new_key] == dict[next]:
                            region.append(new_key)
                            next_nexts.append(new_key)
                        elif new_key not in dict or new_key not in region:
                            borders.append(new_key)
                    dict[next] = 1
                nexts = next_nexts
            groups.append((region, borders))

    if part == 2:
        return sum(len(group[0]) * extend_region(group[0], group[1]) for group in groups)
    return sum([len(group[0]) * len(group[1]) for group in groups])
        
