import re

def compute(content):
    regexp = r'mul\(([0-9]+),([0-9]+)\)'
    result = 0
    for line in content:
        matches = re.findall(regexp, line)
        for match in matches:
            result+= int(match[0]) * int(match[1])
    return result

def compute2(content):
    sum = 0
    content = [line.rstrip() for line in content]
    splits = ''.join(content).split('do()')
    for split in splits:
        split = split.split('don\'t()')
        sum += compute([split[0]])
    return sum