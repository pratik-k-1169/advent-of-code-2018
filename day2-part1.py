#!/usr/bin/env python3
import collections

number_three = 0
number_two = 0

with open("checksum.txt") as f:
    for s in f:
        c = collections.Counter(s)
        if 3 in c.values():
            number_three = number_three + 1
        if 2 in c.values():
            number_two = number_two + 1

print(number_three*number_two)