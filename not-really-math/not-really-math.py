import math


def add(string):
    numbers = string.split('a')
    answer = 0
    for number in numbers:
        answer += int(number)
    return answer


text = ''
answer = 1

splitted = text.split('m')

for string in splitted:
    if 'a' in string:
        answer *= add(string)
    else:
        answer *= int(string)
    answer = answer % (pow(2, 32) - 1)
print(answer % (pow(2, 32) - 1))
