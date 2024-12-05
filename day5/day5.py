def compute(content):
    sum = 0
    rules, prints = extract_content(content)
    for print in prints:
        if check_rules(rules, print):
            sum += print[len(print) // 2]
    return sum

def compute2(content):
    sum = 0
    prints_to_fix = []
    rules, prints = extract_content(content)
    for print in prints:
        if not check_rules(rules, print):
            prints_to_fix.append(print)
    for print in prints_to_fix:
        sum += fix_print(rules, print)
    return sum

def extract_content(content):
    rules = []
    prints = []
    for line in content:
        if '|' in line:
            rules.append([int(element) for element in line.split('|')])
        elif ',' in line:
            prints.append([int(element) for element in line.split(',')])
    return rules, prints

def fix_print(rules, print):
    for element in print:
        min_index = print.index(element)
        for rule in rules:
            if element == rule[0] and rule[1] in print:
                if print.index(rule[0]) > print.index(rule[1]):
                    min_index = min(min_index, print.index(rule[1]))
        print.remove(element)
        print.insert(min_index, element)
    return print[len(print) // 2]

def check_rules(rules, print):
    for element in print:
        for rule in rules:
            if element == rule[0] and rule[1] in print:
                if print.index(rule[0]) > print.index(rule[1]):
                    return False
    return True