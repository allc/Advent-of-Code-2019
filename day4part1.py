'''
https://adventofcode.com/2019/day/3

Usage: python3 day4part1.py
'''


mi, ma = map(int, input().split('-'))


def is_adj_same(n):
    n = str(n)
    last = n[0]
    for c in n[1:]:
        if c == last:
            return True
        last = c
    return False


def is_non_increasing(n):
    n = str(n)
    last = n[0]
    for c in n[1:]:
        if c < last:
            return False
        last = c
    return True


count = 0
for n in range(mi, ma + 1):
    if is_adj_same(n) and is_non_increasing(n):
        count += 1
print(count)
