directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def compute(content, part=1):
    dict = {}
    starts = []
    for i, line in enumerate(content):
        line = line.rstrip()
        for j, element in enumerate(line):
            if element != '.':
                dict[(i, j)] = int(element)
                if dict[(i, j)] == 0:
                    starts.append((i, j))
    nexts = {}
    for key in dict:
        nexts[key] = []
        for direction in directions:
            new_key = key[0] + direction[0], key[1] + direction[1]
            if new_key in dict and dict[key] + 1 == dict[new_key]:
                nexts[key].append(new_key)
    
    final_trails = []
    for start in starts:
        trails = [[start]]
        while(True):
            loop = False
            new_trails = []
            for trail in trails:
                for next in nexts[trail[-1]]:
                    new_trail = trail.copy()
                    new_trail.append(next)
                    new_trails.append(new_trail)
                    loop = True
            if loop:
                trails = new_trails.copy()
            if not loop:
                final_trails.append(trails)
                break
    sum = 0
    if part == 1:
        for element in final_trails:
            ends = set([trail[-1] for trail in element])
            sum += len(ends)
    else:
        for element in final_trails:
            sum += len(element)
    return sum