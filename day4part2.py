'''
https://adventofcode.com/2019/day/3

Usage: python3 day4part2.py
'''


mi, ma = map(int, input().split('-'))


def is_adj_pair(n):
    n = str(n)
    lc = 1
    last = n[0]
    for c in n[1:]:
        if c == last:
            lc += 1
        else:
            if lc == 2:
                return True
            lc = 1
        last = c
    if lc == 2:
        return True
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
    if is_adj_pair(n) and is_non_increasing(n):
        count += 1
print(count)
