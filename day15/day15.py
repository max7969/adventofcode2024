import time

directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def read_content(content):
    map = {}
    robot = (0,0)
    moves = ''
    for i, line in enumerate(content):
        line = line.rstrip()
        if '<' in line or '>' in line or '^' in line or 'v' in line:
            moves += line
        else:
            for j, element in enumerate(line):
                map[(i, j)] = element
                if element == '@':
                    robot = (i, j)
    return robot, moves, map


def move_element(robot, element, direction, map):
    dir = directions[direction]
    new_possible_position = (element[0] + dir[0], element[1] + dir[1])
    if map[new_possible_position] == '.':
        if map[element] == '@':
            robot = new_possible_position
        map[new_possible_position] = map[element]
        map[element] = '.'
        return robot, map, True
    elif map[new_possible_position] == '#':
        return robot, map, False
    else:
        robot, map, moved = move_element(robot, new_possible_position, direction, map)
        if moved:
            robot, map, moved = move_element(robot, element, direction, map)
        return robot, map, moved
        
def move_element_complex(robot, element, direction, map, force=False):
    if direction == '<' or direction == '>':
        return move_element(robot, element, direction, map)
    else:
        dir = directions[direction]
        new_possible_position = (element[0] + dir[0], element[1] + dir[1])
        new_possible_position_right = (new_possible_position[0], new_possible_position[1] + 1)
        new_possible_position_left = (new_possible_position[0], new_possible_position[1] - 1)
        if map[new_possible_position] == '.':
            possible = False
            if map[element] == '@':
                robot = new_possible_position
                possible = True
            elif map[element] == '[':
                right = (element[0], element[1] + 1)
                if map[right] == ']' and not force:
                    robot, map, moved = move_element_complex(robot, right, direction, map, True)
                    possible = moved
                else:
                    possible = True
            elif map[element] == ']':
                left = (element[0], element[1] - 1)
                if map[left] == '[' and not force:
                    robot, map, moved = move_element_complex(robot, left, direction, map, True)
                    possible = moved
                else:
                    possible = True
            if possible:
                map[new_possible_position] = map[element]
                map[element] = '.'
            return robot, map, possible
        elif map[new_possible_position] == '#':
            return robot, map, False
        elif map[element] == '[' and map[new_possible_position_right] == '#':
            return robot, map, False
        elif map[element] == ']' and map[new_possible_position_left] == '#':
            return robot, map, False
        else:
            robot, map, moved = move_element_complex(robot, new_possible_position, direction, map)
            if moved:
                robot, map, moved = move_element_complex(robot, element, direction, map, force)
            return robot, map, moved


def print_map(map):
    for i in range(max([element[0] for element in map.keys()]) + 1):
        line = ''
        for j in range(max([element[1] for element in map.keys()]) + 1):
            line += map[(i, j)]
        print(line)

def compute(content):
    robot, moves, map = read_content(content)
    for move in moves:
        robot, map, moved = move_element(robot, robot, move, map)
    sum = 0
    for element in map:
        if map[element] == 'O':
            sum += element[0] * 100 + element[1]
    return sum

def complete_content(content):
    new_content = []
    for line in content:
        new_line = ''
        for element in line:
            if element == '@':
                new_line += '@.'
            elif element == '#':
                new_line += '##'
            elif element == '.':
                new_line += '..'
            elif element == 'O':
                new_line += '[]'
            else:
                new_line += element
        new_content.append(new_line)
    return new_content

def compute2(content):
    content = complete_content(content)
    robot, moves, map = read_content(content)
    for i, move in enumerate(moves):
        copy_map = map.copy()
        robot, map, moved = move_element_complex(robot, robot, move, map)
        if not moved:
            map = copy_map
    print_map(map)
    sum = 0
    for element in map:
        if map[element] == '[':
            sum += element[0] * 100 + element[1]
    return sum