directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def extract_map(content):
    dict = {}
    current_pos = (0, 0)
    for i, line in enumerate(content):
        for j, char in enumerate(line.rstrip()):
            if char == '<':
                dict[(i, j)] = '.'
                current_pos = (i, j, directions[0])
            elif char == '^':
                dict[(i, j)] = '.'
                current_pos = (i, j, directions[1])
            elif char == '>':
                dict[(i, j)] = '.'
                current_pos = (i, j, directions[2])
            elif char == 'v':
                dict[(i, j)] = '.'
                current_pos = (i, j, directions[3])
            else:
                dict[(i, j)] = char
    return dict, current_pos

def move_guard(dict, current_pos):
    visited_pos = {}
    is_cycle = True
    while current_pos not in visited_pos.keys():
        visited_pos[current_pos] = (current_pos[0], current_pos[1])
        next_pos = (current_pos[0] + current_pos[2][0], current_pos[1] + current_pos[2][1])
        if next_pos not in dict.keys():
            is_cycle = False
            break
        elif dict[next_pos] == '.':
            current_pos = (next_pos[0], next_pos[1], current_pos[2])
        elif dict[next_pos] == '#':
            new_dir = directions[(directions.index(current_pos[2]) + 1) % 4]
            current_pos = (current_pos[0], current_pos[1], new_dir)
    return len(set(visited_pos.values())), is_cycle, set(visited_pos.values())

def compute(content):
    sum = 0
    dict, current_pos = extract_map(content)
    result = move_guard(dict, current_pos)
            
    return result[0]


def compute2(content):
    sum = 0
    dict, current_pos = extract_map(content)
    count_classic, cycle, visisted = move_guard(dict.copy(), current_pos)
    visisted.remove((current_pos[0], current_pos[1]))
    list_pos = []
    for pos in visisted:
        copy = dict.copy()
        copy[pos] = '#'
        _, is_cycle, _ = move_guard(copy, current_pos)
        if is_cycle:
            list_pos.append(pos)
            sum += 1
    return sum
