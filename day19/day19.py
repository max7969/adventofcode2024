from functools import lru_cache

def read_content(content):
    towels = []
    patterns = []

    towels = content[0].rstrip().split(', ')
    for i in range (2, len(content)):
        patterns.append(content[i].rstrip())
    return towels, patterns

@lru_cache(maxsize=None)
def treat_pattern(pattern, towels):
    sum = 0
    for towel in towels:
        if pattern.startswith(towel):
            if len(pattern) == len(towel):
                sum += 1
            else:
                sum += treat_pattern(pattern[len(towel):], towels)
    return sum

def compute(content, part=1):
    towels, patterns = read_content(content)
    sum = 0
    for pattern in patterns:
        result = treat_pattern(pattern, tuple(towels))
        if result > 0:
            if part == 1:
                sum += 1
            else:
                sum += result
    return sum