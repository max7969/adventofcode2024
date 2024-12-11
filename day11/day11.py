def get_new_stones(stone):
    new_stones = []
    if stone == '0':
        new_stones.append('1')
    elif len(stone) % 2 == 0:
        new_stones.append(str(int(stone[:(len(stone) // 2)])))
        new_stones.append(str(int(stone[(len(stone) // 2):])))
    else:
        new_stones.append(str(int(stone) * 2024))
    return new_stones

def compute(content, iterations):
    stones = content[0].rstrip().split(' ')
    dict = {}
    for stone in stones:
        if stone in dict:
            dict[stone] += 1
        else:
            dict[stone] = 1
    for i in range(iterations):
        copy_dict = dict.copy()
        for key in dict:
            new_stones = get_new_stones(key)
            for stone in new_stones:
                if stone in copy_dict:
                    copy_dict[stone] += dict[key]
                else:
                    copy_dict[stone] = dict[key]
            copy_dict[key] -= dict[key]
        for key in [key for key in copy_dict if copy_dict[key] == 0]:
            del copy_dict[key]
        dict = copy_dict
    return sum([dict[key] for key in dict])