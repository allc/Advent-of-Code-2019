'''
https://adventofcode.com/2019/day/3

Usage: cat day3input.txt | python3 day3part1.py
'''


wire1r = list(input().split(','))
wire2r = list(input().split(','))


wire1 = set()
p = (0, 0)
for w in wire1r:
    if w[0] == 'R':
        for _ in range(int(w[1:])):
            p = (p[0] + 1, p[1])
            wire1.add(p)
    elif w[0] == 'D':
        for _ in range(int(w[1:])):
            p = (p[0], p[1] - 1)
            wire1.add(p)
    elif w[0] == 'L':
        for _ in range(int(w[1:])):
            p = (p[0] - 1, p[1])
            wire1.add(p)
    elif w[0] == 'U':
        for _ in range(int(w[1:])):
            p = (p[0], p[1] + 1)
            wire1.add(p)


wire2 = set()
p = (0, 0)
for w in wire2r:
    if w[0] == 'R':
        for _ in range(int(w[1:])):
            p = (p[0] + 1, p[1])
            wire2.add(p)
    elif w[0] == 'D':
        for _ in range(int(w[1:])):
            p = (p[0], p[1] - 1)
            wire2.add(p)
    elif w[0] == 'L':
        for _ in range(int(w[1:])):
            p = (p[0] - 1, p[1])
            wire2.add(p)
    elif w[0] == 'U':
        for _ in range(int(w[1:])):
            p = (p[0], p[1] + 1)
            wire2.add(p)


intersects = wire1 & wire2


min_dist = float('inf')
for intersect in intersects:
    min_dist = min(min_dist, abs(intersect[0]) + abs(intersect[1]))
print(min_dist)
