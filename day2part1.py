'''
https://adventofcode.com/2019/day/2

Usage: cat day2part1input.txt | python3 day2part1.py
'''


REPLACE = True


l = list(map(int, input().split(',')))
if REPLACE:
    l[1] = 12
    l[2] = 2
for i in range(0, len(l), 4):
    if l[i] == 1:
        l[l[i + 3]] = l[l[i + 1]] + l[l[i + 2]]
    elif l[i] == 2:
        l[l[i + 3]] = l[l[i + 1]] * l[l[i + 2]]
    elif l[i] == 99:
        break
print(l[0])
