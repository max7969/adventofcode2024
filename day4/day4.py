config = {}
config[1] = {
    'center': 'X',
    'possibilities': [
        [{'x': -1, 'y':-1}, {'x': -2, 'y':-2}, {'x': -3, 'y':-3}],
        [{'x': -1, 'y':0}, {'x': -2, 'y':0}, {'x': -3, 'y':0}],
        [{'x': -1, 'y':1}, {'x': -2, 'y':2}, {'x': -3, 'y':3}],
        [{'x': 0, 'y':1}, {'x': 0, 'y':2}, {'x': 0, 'y':3}],
        [{'x': 1, 'y':1}, {'x': 2, 'y':2}, {'x': 3, 'y':3}],
        [{'x': 1, 'y':0}, {'x': 2, 'y':0}, {'x': 3, 'y':0}],
        [{'x': 1, 'y':-1}, {'x': 2, 'y':-2}, {'x': 3, 'y':-3}],
        [{'x': 0, 'y':-1}, {'x': 0, 'y':-2}, {'x': 0, 'y':-3}]
    ],
    'chain': 'MAS'
}
config[2] = {
    'center': 'A',
    'possibilities': [
        [{'x': -1, 'y':-1}, {'x': -1, 'y':1}, {'x': 1, 'y':1}, {'x': 1, 'y':-1}],
        [{'x': 1, 'y':-1}, {'x': -1, 'y':-1}, {'x': -1, 'y':1}, {'x': 1, 'y':1}],
        [{'x': 1, 'y':1}, {'x': 1, 'y':-1}, {'x': -1, 'y':-1}, {'x': -1, 'y':1}],
        [{'x': -1, 'y':1}, {'x': 1, 'y':1}, {'x': 1, 'y':-1}, {'x': -1, 'y':-1}]
    ],
    'chain': 'MMSS'
}

def compute(content, part=1):
    dict = {}
    for i in range(len(content)):
        for j in range(len(content[i])):
            dict[str(i) + ',' + str(j)] = content[i][j]

    sum = 0
    for key in dict:
        if dict[key] == config[part]['center']:
            x_i, x_j = int(key.split(',')[0]), int(key.split(',')[1])
            for possibility in config[part]['possibilities']:
                result = ''
                for p in possibility:
                    i, j = x_i + p['x'], x_j + p['y']
                    if (str(i) + ',' + str(j)) in dict.keys():
                        result += dict[str(i) + ',' + str(j)]
                if result == config[part]['chain']:
                    sum += 1
    return sum