def calculate_antinodes(antenna1, antenna2, max_x, max_y):
    antinode1, antinode2 = [-1,-1], [-1,-1]
    for i in range(2):
        if antenna1[i] < antenna2[i]:
            antinode1[i] = antenna1[i] - abs(antenna1[i] - antenna2[i])
            antinode2[i] = antenna2[i] + abs(antenna1[i] - antenna2[i])
        elif antenna1[i] > antenna2[i]:
            antinode1[i] = antenna1[i] + abs(antenna1[i] - antenna2[i])
            antinode2[i] = antenna2[i] - abs(antenna1[i] - antenna2[i])
        else:
            antinode1[i] = antenna1[i]
            antinode2[i] = antenna2[i]
    if antinode1[0] < 0 or antinode1[0] >= max_x or antinode1[1] < 0 or antinode1[1] >= max_y:
        antinode1 = [-1,-1]
    if antinode2[0] < 0 or antinode2[0] >= max_x or antinode2[1] < 0 or antinode2[1] >= max_y:
        antinode2 = [-1,-1]
    return antinode1, antinode2

def read_content(content):
    dict = {}
    for i, line in enumerate(content):
        line = line.rstrip()
        for j, element in enumerate(line):
            if element != '.':
                if element not in dict:
                    dict[element] = [(i,j)]
                else:
                    dict[element].append((i,j))
    return dict

def compute(content):
    dict = read_content(content)
    antinodes = []
    for key in dict:
        for antenna in dict[key]:
            for antenna2 in dict[key]:
                if antenna != antenna2:
                    antinode1, antinode2 = calculate_antinodes(antenna, antenna2, len(content), len(content[0].rstrip()))
                    if antinode1 != [-1,-1]:
                        antinodes.append(antinode1)
                    if antinode2 != [-1,-1]:
                        antinodes.append(antinode2)
    set_antinodes = set([(antinode[0], antinode[1]) for antinode in antinodes])

    return len(set_antinodes)

def compute_antinodes(antenna1, antenna2, max_x, max_y):
    antinodes = set()
    diff_x = antenna1[0] - antenna2[0]
    diff_y = antenna1[1] - antenna2[1]
    for i in range(1, max_x):
        new_antinode = antenna1[0] + diff_x * i, antenna1[1] + diff_y * i
        if new_antinode[0] < 0 or new_antinode[0] >= max_x or new_antinode[1] < 0 or new_antinode[1] >= max_y:
            break
        antinodes.add(new_antinode)
    for i in range(1, max_x):
        new_antinode = antenna1[0] - diff_x * i, antenna1[1] - diff_y * i
        if new_antinode[0] < 0 or new_antinode[0] >= max_x or new_antinode[1] < 0 or new_antinode[1] >= max_y:
            break
        antinodes.add(new_antinode)
    antinodes.add(antenna1)
    return list(antinodes)

def compute2(content):
    dict = read_content(content)
    antinodes = []
    for key in dict:
        for antenna in dict[key]:
            for antenna2 in dict[key]:
                if antenna != antenna2:
                    antinodes.extend(compute_antinodes(antenna, antenna2, len(content), len(content[0].rstrip())))
    return len(set(antinodes))
