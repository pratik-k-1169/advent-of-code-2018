#!/usr/bin/env python3

ids = []
with open("checksum.txt") as f:
    for s in f:
        s = s.strip()
        ids.append(s)

def scan(s1,s2):
    diff = 0
    for i,j in zip(s1,s2):
        if diff <= 1:
            if i != j:
                diff = diff + 1
        else:
            break
    if diff <= 1:
        return True
    return False

s = ""
for i in range(len(ids)):
    for j in range(i+1,len(ids)):
        if scan(ids[i],ids[j]):
            for letter_i,letter_j in zip(ids[i],ids[j]):
                if letter_i == letter_j:
                    s = s + letter_i

print(s)