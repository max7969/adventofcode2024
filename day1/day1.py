def compute(content):
    group1 = sorted([element.rstrip().split('   ')[0] for element in content])
    group2 = sorted([element.rstrip().split('   ')[1] for element in content])
    sum = 0
    for i in range(len(group1)):
        sum += abs(int(group1[i]) - int(group2[i]))

    return sum

def compute2(content):
    group1 = sorted([element.rstrip().split('   ')[0] for element in content])
    group2 = sorted([element.rstrip().split('   ')[1] for element in content])
    sum = 0
    for element in group1:
        sum += int(element) * group2.count(element)

    return sum