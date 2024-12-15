def move_robot(robot, size):
    x, y = robot['position']
    mx, my = robot['velocity']
    robot['position'] = (x + mx, y + my)
    if robot['position'][0] < 0:
        robot['position'] = (size[0] + robot['position'][0], robot['position'][1])
    if robot['position'][1] < 0:
        robot['position'] = (robot['position'][0], size[1] + robot['position'][1])
    if robot['position'][0] >= size[0]:
        robot['position'] = (robot['position'][0] - size[0], robot['position'][1])
    if robot['position'][1] >= size[1]:
        robot['position'] = (robot['position'][0], robot['position'][1] - size[1])
    return robot

def safety_factor(robots, size):
    factors = [0,0,0,0]
    for robot in robots:
        if robot['position'][0] < size[0] // 2 and robot['position'][1] < size[1] // 2:
            factors[0] += 1
        elif robot['position'][0] < size[0] // 2 and robot['position'][1] > size[1] // 2:
            factors[1] += 1
        elif robot['position'][0] > size[0] // 2 and robot['position'][1] < size[1] // 2:
            factors[2] += 1
        elif robot['position'][0] > size[0] // 2 and robot['position'][1] > size[1] // 2:
            factors[3] += 1
    return factors[0] * factors[1] * factors[2] * factors[3]

def print_robots(robots, size):
    for i in range(size[1]):
        line = ''
        for j in range(size[0]):
            if (j, i) in [robot['position'] for robot in robots]:
                line += '#'
            else:
                line += '.'
        print(line)

def check_sum_robots(robots, size):
    checksum = ''
    for i in range(size[1]):
        line = ''
        for j in range(size[0]):
            if (j, i) in [robot['position'] for robot in robots]:
                line += '#'
            else:
                line += '.'
        checksum += line
    return checksum

def read_content(content):
    robots = []
    for line in content:
        line = line.rstrip()
        split = line.split(' ')

        x, y = int(split[0].split('p=')[1].split(',')[0]), int(split[0].split('p=')[1].split(',')[1])
        mx, my = int(split[1].split('v=')[1].split(',')[0]), int(split[1].split('v=')[1].split(',')[1])
        robots.append({'position': (x, y), 'velocity': (mx, my)})

    size = max([robot['position'][0] for robot in robots]) + 1, max([robot['position'][1] for robot in robots]) + 1
    return robots, size

def compute(content):
    robots, size = read_content(content)
    for i in range(100):
        for robot in robots:
            robot = move_robot(robot, size)
    return safety_factor(robots, size)

def might_be_christmas_tree(robots, size):
    line = [(0, -1), (0, -2), (0, 1), (0, 2)]
    robots_positions = [robot['position'] for robot in robots]
    line_of_robots = 0
    for robot in robots:
        count = 1
        for l in line:
            if (robot['position'][0] + l[0], robot['position'][1] + l[1]) in robots_positions:
                count += 1
        if count == 5:
            line_of_robots += 1
    return line_of_robots > 7

def compute2(content):
    robots, size = read_content(content)
    seconds = 0
    while True:
        for robot in robots:
            robot = move_robot(robot, size)
        seconds += 1
        if might_be_christmas_tree(robots, size):
            print_robots(robots, size)
            print("seconds:" + str(seconds))
            break
    return seconds