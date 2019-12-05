'''
https://adventofcode.com/2019/day/3

Usage: cat day3input.txt | python3 day3part2.py
'''


wire1r = list(input().split(','))
wire2r = list(input().split(','))


wire1 = dict()
p = (0, 0)
d = 0
for w in wire1r:
    if w[0] == 'R':
        for _ in range(int(w[1:])):
            p = (p[0] + 1, p[1])
            d += 1
            if p not in wire1:
                wire1[p] = d
    elif w[0] == 'D':
        for _ in range(int(w[1:])):
            p = (p[0], p[1] - 1)
            d += 1
            if p not in wire1:
                wire1[p] = d
    elif w[0] == 'L':
        for _ in range(int(w[1:])):
            p = (p[0] - 1, p[1])
            d += 1
            if p not in wire1:
                wire1[p] = d
    elif w[0] == 'U':
        for _ in range(int(w[1:])):
            p = (p[0], p[1] + 1)
            d += 1
            if p not in wire1:
                wire1[p] = d


wire2 = dict()
p = (0, 0)
d = 0
for w in wire2r:
    if w[0] == 'R':
        for _ in range(int(w[1:])):
            p = (p[0] + 1, p[1])
            d += 1
            if p not in wire2:
                wire2[p] = d
    elif w[0] == 'D':
        for _ in range(int(w[1:])):
            p = (p[0], p[1] - 1)
            d += 1
            if p not in wire2:
                wire2[p] = d
    elif w[0] == 'L':
        for _ in range(int(w[1:])):
            p = (p[0] - 1, p[1])
            d += 1
            if p not in wire2:
                wire2[p] = d
    elif w[0] == 'U':
        for _ in range(int(w[1:])):
            p = (p[0], p[1] + 1)
            d += 1
            if p not in wire2:
                wire2[p] = d


intersects = wire1.keys() & wire2.keys()


min_dist = float('inf')
for intersect in intersects:
    min_dist = min(min_dist, wire1[intersect] + wire2[intersect])
print(min_dist)
