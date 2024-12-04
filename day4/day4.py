center_p1 = 'X'
center_p2 = 'A'
possibilities_p1 = [
        [{'x': -1, 'y':-1}, {'x': -2, 'y':-2}, {'x': -3, 'y':-3}],
        [{'x': -1, 'y':0}, {'x': -2, 'y':0}, {'x': -3, 'y':0}],
        [{'x': -1, 'y':1}, {'x': -2, 'y':2}, {'x': -3, 'y':3}],
        [{'x': 0, 'y':1}, {'x': 0, 'y':2}, {'x': 0, 'y':3}],
        [{'x': 1, 'y':1}, {'x': 2, 'y':2}, {'x': 3, 'y':3}],
        [{'x': 1, 'y':0}, {'x': 2, 'y':0}, {'x': 3, 'y':0}],
        [{'x': 1, 'y':-1}, {'x': 2, 'y':-2}, {'x': 3, 'y':-3}],
        [{'x': 0, 'y':-1}, {'x': 0, 'y':-2}, {'x': 0, 'y':-3}]
    ]
possibilities_p2 = [
        [{'x': -1, 'y':-1}, {'x': -1, 'y':1}, {'x': 1, 'y':1}, {'x': 1, 'y':-1}],
        [{'x': 1, 'y':-1}, {'x': -1, 'y':-1}, {'x': -1, 'y':1}, {'x': 1, 'y':1}],
        [{'x': 1, 'y':1}, {'x': 1, 'y':-1}, {'x': -1, 'y':-1}, {'x': -1, 'y':1}],
        [{'x': -1, 'y':1}, {'x': 1, 'y':1}, {'x': 1, 'y':-1}, {'x': -1, 'y':-1}]
    ]
chain_p1 = 'MAS'
chain_p2 = 'MMSS'

def compute(content, part=1):
    dict = {}
    for i in range(len(content)):
        for j in range(len(content[i])):
            dict[str(i) + ',' + str(j)] = content[i][j]
    possibilities = possibilities_p1
    chain = chain_p1
    center = center_p1
    if part == 2:
        possibilities = possibilities_p2
        chain = chain_p2
        center = center_p2

    sum = 0
    for key in dict:
        if dict[key] == center:
            x_i, x_j = int(key.split(',')[0]), int(key.split(',')[1])
            for possibility in possibilities:
                result = ''
                for p in possibility:
                    i, j = x_i + p['x'], x_j + p['y']
                    if (str(i) + ',' + str(j)) in dict.keys():
                        result += dict[str(i) + ',' + str(j)]
                if result == chain:
                    sum += 1
    return sum