import re
handle = open("regex_sum_76404.txt")
total = 0

for line in handle:
    y = (re.findall('[0-9]+', line))
    for number in y:
        number = int(number)
        total = total + number

print(total)
