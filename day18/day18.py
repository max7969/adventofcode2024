import heapq

def heuristic(a, b):
    # Manhattan distance heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(map, node):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direction in directions:
        neighbor = (node[0] + direction[0], node[1] + direction[1])
        if neighbor in map and map[neighbor] != '#':
            neighbors.append(neighbor)
    return neighbors

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def shortest_path(map, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == end:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(map, current):
            tentative_g_score = g_score[current] + 1  # Assuming each move has a cost of 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def read_input(content, falling):
    map = {}
    bytes = []
    for line in content:
        line = line.rstrip()
        split = line.split(',')    
        bytes.append((int(split[1]), int(split[0])))

    max_x = max([x[0] for x in bytes])
    max_y = max([x[1] for x in bytes])

    for i in range(max_x + 1):
        for j in range(max_y + 1):
            map[(i, j)] = '.'

    for i in range(falling):
        map[bytes[i]] = '#'
    return map, max_x, max_y, bytes


def compute(content, falling = 1024):
    map, max_x, max_y, bytes = read_input(content, falling)

    path = shortest_path(map, (0, 0), (max_x, max_y))
    return len(path) - 1

def compute2(content):
    max_bytes = len(content)
    for i in range(max_bytes):
        map, max_x, max_y, bytes = read_input(content, i)
        path = shortest_path(map, (0, 0), (max_x, max_y))
        if path is None:
            return str(bytes[i - 1][1]) + "," + str(bytes[i - 1][0])
    return "0,0"