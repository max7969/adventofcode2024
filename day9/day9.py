def init(line):
    values, fills, memory = [], [], []
    for index, element in enumerate(line):
        if index % 2 == 0:
            values.append(int(element))
        else:
            fills.append(int(element))
    return values, fills, memory


def compute(content):
    line = content[0].rstrip()
    values, fills, memory = init(line)
    i = 0
    while sum(values) > 0:
        for j in range(values[i]):
            memory.append(i)
            values[i] -= 1
        for j in range(fills[i]):
            if values[len(values) - 1] > 0:
                memory.append(len(values) - 1)
                values[len(values) - 1] -= 1
            elif values[len(values) - 2] > 0:
                values = values[:len(values) - 1]
                memory.append(len(values) - 1)
                values[len(values) - 1] -= 1
        i += 1
    result = 0
    for i in range(len(memory)):
        result += memory[i] * i
    return result

def compute2(content):
    line = content[0].rstrip()
    values, fills, memory = init(line)
    copy_values = values.copy()

    i = len(values) - 1
    for i in range(len(values)):
        if values[i] == copy_values[i]:
            for j in range(values[i]):
                memory.append(i)
                values[i] -= 1
        else:
            for j in range(copy_values[i]):
                memory.append(0)

        if i < len(fills):
            for j in range(len(values) -1, 0, -1):
                if values[j] <= fills[i]:
                    for k in range(values[j]):
                        memory.append(j)
                        values[j] -= 1
                        fills[i] -= 1
            if fills[i] > 0:
                for j in range(fills[i]):
                    memory.append(0)
    
    result = 0
    for i in range(len(memory)):
        result += memory[i] * i
    return result
