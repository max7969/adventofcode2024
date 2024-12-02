def compute(content):
    all_numbers = [[int(number) for number in element.rstrip().split(' ')] for element in content]
    return check(all_numbers)

def compute2(content):
    all_numbers = [[int(number) for number in element.rstrip().split(' ')] for element in content]
    sum = 0
    for number in all_numbers:
        first_check = check([number])
        if first_check == 1:
            sum += 1
        else:
            alternative_numbers = []
            for i in range(len(number)):
                temp = number.copy()
                temp.pop(i)
                alternative_numbers.append(temp)
            sum += 1 if check(alternative_numbers) >= 1 else 0
    return sum

def check(all_numbers):
    sum = 0
    for numbers in all_numbers:
        diff = []
        for i in range(1, len(numbers)):
            diff.append(numbers[i] - numbers[i-1])
        
        if ((len(list(filter(lambda x: x > 0 and x <= 3, diff))) == len(diff)) 
            or (len(list(filter(lambda x: x < 0 and x >= -3, diff))) == len(diff))):
            sum += 1
    return sum