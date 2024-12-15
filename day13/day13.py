def calculate_solution(a, b, p):
    max_best = min(p[0] // a[0], p[1] // a[1])
    for i in range(max_best, 0, -1):
        restX = p[0] - (a[0] * i)
        restY = p[1] - (a[1] * i)

        if restX % b[0] == 0 and restY % b[1] == 0:
            if restX // b[0] == restY // b[1]:
                return {'best_button': i, 'worst_button': restX // b[0]}
    return None

def compute(content):
    machines = []
    current = {}
    for line in content:
        line = line.rstrip()
        split = line.split(': ')
        if split[0] == 'Button A':
            current['A'] = [int(split[1].split(', ')[0].split('+')[1]), int(split[1].split(', ')[1].split('+')[1])]
        elif split[0] == 'Button B':
            current['B'] = [int(split[1].split(', ')[0].split('+')[1]), int(split[1].split(', ')[1].split('+')[1])]
        elif split[0] == 'Prize':
            current['P'] = [int(split[1].split(', ')[0].split('=')[1]), int(split[1].split(', ')[1].split('=')[1])]
        else:
            machines.append(current.copy())
            current = {}

    for machine in machines:
        best_button = 'B'
        worst_button = 'A'
        if sum(machine['A']) / 3 >= sum(machine['B']):
            best_button = 'A'
            worst_button = 'B'

        result = calculate_solution(machine[best_button], machine[worst_button], machine['P'])
        if result is not None:
            machine['solution'] = {best_button: result['best_button'], worst_button: result['worst_button']}

    result = 0
    for machine in machines:
        if 'solution' in machine:
            result += machine['solution']['A'] * 3 + machine['solution']['B'] 
    return result

def compute2(content):
    addition = 10000000000000
    machines = []
    current = {}
    for line in content:
        line = line.rstrip()
        split = line.split(': ')
        if split[0] == 'Button A':
            current['A'] = [int(split[1].split(', ')[0].split('+')[1]), int(split[1].split(', ')[1].split('+')[1])]
        elif split[0] == 'Button B':
            current['B'] = [int(split[1].split(', ')[0].split('+')[1]), int(split[1].split(', ')[1].split('+')[1])]
        elif split[0] == 'Prize':
            current['P'] = [int(split[1].split(', ')[0].split('=')[1]) + addition, int(split[1].split(', ')[1].split('=')[1]) + addition]
        else:
            machines.append(current.copy())
            current = {}
    machines.append(current.copy())

    result = 0
    for machine in machines:
        z1 = machine['P'][0]
        z2 = machine['P'][1]    

        x1 = machine['A'][0]
        x2 = machine['A'][1]

        y1 = machine['B'][0]
        y2 = machine['B'][1]

        b = (z2 * x1 - z1 * x2) // (y2 * x1 - y1 * x2)
        a = (z1 - b * y1) // x1
        if (x1 * a + y1 * b, x2 * a + y2 * b) != (z1, z2):
            result += 0
        else: 
           result += a * 3 + b
    
    return result