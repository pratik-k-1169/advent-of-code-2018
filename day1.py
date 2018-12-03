#!/usr/bin/env python3
with open("numbers.txt") as f:
    sum = 0
    lst = []
    for number in f:
        number = number.strip()
        lst.append(number)

i = 0
sums = set()
sum = 0
while(1):
    try:
        if lst[i].startswith('+'):
            sum = sum + int(lst[i][1:])
        else:
            sum = sum - int(lst[i][1:])
        if sum not in sums:
            sums.add(sum)
        else:
            print(f"Repeat: {sum}")
            break
        i = i + 1
    except IndexError:
        i = 0

