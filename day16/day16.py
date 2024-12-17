import heapq
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor
import os

facing = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def heuristic(node, end):
    return abs(node[0] - end[0]) + abs(node[1] - end[1])

def next_nodes(node, cost, map):
    new_nodes = []
    move = (node[0] + facing[node[2]][0], node[1] + facing[node[2]][1], node[2])
    if map[(move[0], move[1])] == '.':
        new_nodes.append((cost + 1, move))
    move2 = (node[0] + facing[(node[2] + 1) % 4][0], node[1] + facing[(node[2] + 1) % 4][1], (node[2] + 1) % 4)
    move3 = (node[0] + facing[(node[2] - 1) % 4][0], node[1] + facing[(node[2] - 1) % 4][1], (node[2] - 1) % 4)
    move4 = (node[0] + facing[(node[2] + 2) % 4][0], node[1] + facing[(node[2] + 2) % 4][1], (node[2] + 2) % 4)
    if map[(move2[0], move2[1])] == '.':
        new_nodes.append((cost + 1001, move2))
    if map[(move3[0], move3[1])] == '.':
        new_nodes.append((cost + 1001, move3))
    if map[(move4[0], move4[1])] == '.':
        new_nodes.append((cost + 2001, move4))
    return tuple(new_nodes)

def build_path(came_from, current):
    current = current[1]
    path = [current]
    while current in came_from: 
        current = came_from[current][1]
        path.append(current)
    return path[::-1]

def compute_best_path(map, start, end, compute_best = True):
    nodes = []
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    came_from = {}
    heapq.heappush(nodes, (f_score[start], start, g_score[start]))
    visited = set()
    while nodes:
        current = heapq.heappop(nodes)
        if (current[1][0], current[1][1]) == end:
            if compute_best:
                return current[0], build_path(came_from, current)
            else:
                return current[0], current
            
        if current[1] in visited:
            continue
        visited.add(current[1])

        new_nodes = next_nodes(current[1], current[2], map)
       
        for next in new_nodes:
            if next[1] not in g_score or next[0] < g_score[next[1]]:
                came_from[next[1]] = current
                g_score[next[1]] = next[0]
                f_score[next[1]] = next[0] + heuristic(next[1], end)
                heapq.heappush(nodes, (f_score[next[1]], next[1], g_score[next[1]]))
    return 1000000000000000, None

def read_content(content):
    map = {}
    start = None
    end = None
    for i, line in enumerate(content):
        line = line.rstrip()
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j, 0)
                map[(i, j)] = '.'
            elif c == 'E':
                end = (i, j)
                map[(i, j)] = '.'
            else:
                map[(i, j)] = c
    return map, start, end

def compute(content):
    map, start, end = read_content(content)
    return compute_best_path(map, start, end)[0]

def print_map(map, treated):
    for i in range(max([element[0] for element in map.keys()]) + 1):
        line = ''
        for j in range(max([element[1] for element in map.keys()]) + 1):
            if (i, j) in treated:
                line += 'O'
            else:
                line += map[(i, j)]
        print(line)




def compute2(content):
    map, start, end = read_content(content)
    score, path = compute_best_path(map, start, end)
    
    def process_element(element):
        if map[element] == '.':
            scoreA, currentA = compute_best_path(map, start, element, False)
            if scoreA <= score:
                scoreB, pathB = compute_best_path(map, currentA[1], end, False)
                if scoreA + scoreB == score:
                    print(element)
                    return 1
        print(element)
        return 0

    num_threads = os.cpu_count()  # Number of CPU cores
    print(f"Using {num_threads} threads for parallel processing")

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(process_element, map.keys()))

    return sum(results)


