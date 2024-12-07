def check_with_two_operators(result, values):
    for i in range(2 ** (len(values) - 1)):
        binary_number = bin(i)[2:].zfill(len(values) - 1)
        expression = ''
        evaluation = 0
        for value in values:
            expression += str(value)
            evaluation = eval(expression)
            expression = str(evaluation)
            if len(binary_number) > 0:
                expression += binary_number[0].replace('0', '+').replace('1', '*')  
                binary_number = binary_number[1:]
        if evaluation == result:
            return evaluation
    return 0

def to_base_3(n, length):
    if n == 0:
        return '0' * length
    digits = []
    while n:
        digits.append(int(n % 3))
        n //= 3
    base_3_number = ''.join(str(x) for x in digits[::-1])
    return base_3_number.zfill(length)


def check_with_three_operators(result, values):
    for i in range(3 ** (len(values) - 1)):
        base_three_number = to_base_3(i, len(values) - 1)
        expression = ''
        evaluation = 0
        for value in values:
            expression += str(value)
            evaluation = eval(expression)
            expression = str(evaluation)
            if len(base_three_number) > 0:
                expression += base_three_number[0].replace('0', '+').replace('1', '*').replace('2', '')
                base_three_number = base_three_number[1:]
        if evaluation == result:
            return evaluation
    return 0

def compute(content):
    sum = 0
    for line in content:
        line = line.rstrip()
        result = int(line.split(': ')[0])
        values = [int(x) for x in line.split(': ')[1].split(' ')]
        sum += check_with_two_operators(result, values)
    return sum


def compute2(content):
    sum = 0
    for line in content:
        line = line.rstrip()
        result = int(line.split(': ')[0])
        values = [int(x) for x in line.split(': ')[1].split(' ')]
        evaluation = check_with_two_operators(result, values)
        if evaluation == 0:
            evaluation = check_with_three_operators(result, values)
        sum += evaluation
    return sum
