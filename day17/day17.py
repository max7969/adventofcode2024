def adv(value, register, pointer):
    register['A'] = register['A'] // pow(2, operand(value, register))
    return pointer + 2, None

def bxl(value, register, pointer):
    register['B'] = register['B'] ^ value
    return pointer + 2, None

def bst(value, register, pointer):
    register['B'] = operand(value, register) % 8
    return pointer + 2, None

def jnz(value, register, pointer):
    if register['A'] != 0:
        return value, None
    return pointer + 2, None

def bxc(value, register, pointer):
    register['B'] = register['B'] ^ register['C']
    return pointer + 2, None

def out(value, register, pointer):
    return pointer + 2, operand(value, register) % 8

def bdv(value, register, pointer):
    register['B'] = register['A'] // pow(2, operand(value, register))
    return pointer + 2, None

def cdv(value, register, pointer):
    register['C'] = register['A'] // pow(2, operand(value, register))
    return pointer + 2, None

operations = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

def operand(value, register):
    if value >= 0 and value <= 3:
        return value
    elif value == 4:
        return register['A']
    elif value == 5:
        return register['B']
    elif value == 6:
        return register['C']
    return None

def program_to_string(program):
    return ",".join([str(element) for element in program])

def compute_program(program, register):
    output = []
    instruction_pointer = 0
    while instruction_pointer < len(program) - 1:
        op_code = program[instruction_pointer]
        value = program[instruction_pointer + 1]
        instruction_pointer, value = operations[op_code](value, register, instruction_pointer)
        if value is not None:
            output.append(value)
    return output

def compute_program_part2(program, register, temp):
    output = []
    instruction_pointer = 0
    while instruction_pointer < len(program) - 1:
        op_code = program[instruction_pointer]
        value = program[instruction_pointer + 1]
        instruction_pointer, value = operations[op_code](value, register, instruction_pointer)
        if value is not None:
            output.append(value)
            if not program_to_string(temp).startswith(program_to_string(output)):
                return False
            elif program_to_string(temp) == program_to_string(output):
                return True
    return program_to_string(temp) == program_to_string(output)

def compute(content):
    register = {}
    program = []
    for line in content:
        line = line.rstrip()
        split = line.split(': ')
        if split[0] == 'Register A':
            register['A'] = int(split[1])
        elif split[0] == 'Register B':
            register['B'] = int(split[1])
        elif split[0] == 'Register C':
            register['C'] = int(split[1])
        elif split[0] == 'Program':
            program = [int(element) for element in split[1].split(',')]

    output = compute_program(program, register)

    return ",".join([str(element) for element in output])



def compute2(content):
    register = {}
    program = []
    for line in content:
        line = line.rstrip()
        split = line.split(': ')
        if split[0] == 'Register A':
            register['A'] = int(split[1])
        elif split[0] == 'Register B':
            register['B'] = int(split[1])
        elif split[0] == 'Register C':
            register['C'] = int(split[1])
        elif split[0] == 'Program':
            program = [int(element) for element in split[1].split(',')]
    copy_register = register.copy()

    temp = []
    steps = [1]
    first = 0
    for j in range(0, len(program), 2):
        temp.append(program[j])
        temp.append(program[j+1])
        is_pattern = False
        a = first
        possible_a = []
        pattern = []
        cycle = 0
        while not is_pattern:
            register['A'] = a
            register['B'] = copy_register['B']
            register['C'] = copy_register['C']
            if compute_program_part2(program, register, temp):
                if possible_a == []:
                    first = a
                possible_a.append(a)
                if len(possible_a) > 1:
                    pattern.append(possible_a[-1] - possible_a[-2])
                    if pattern[:(len(pattern) // 2)] == pattern[(len(pattern) // 2):] and len(pattern) > 4:
                        is_pattern = True
                        steps = pattern[:(len(pattern) // 2)]
            a += steps[cycle % len(steps)]
            cycle += 1

    return possible_a[0]
