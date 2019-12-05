'''
https://adventofcode.com/2019/day/2

Usage: cat day2input.txt | python3 day2part2.py
'''


l0 = list(map(int, input().split(',')))
for n in range(100):
    for v in range(100):
        l = l0.copy()
        try:
            l[1] = n
            l[2] = v
            for i in range(0, len(l), 4):
                if l[i] == 1:
                    l[l[i + 3]] = l[l[i + 1]] + l[l[i + 2]]
                elif l[i] == 2:
                    l[l[i + 3]] = l[l[i + 1]] * l[l[i + 2]]
                elif l[i] == 99:
                    break
            if l[0] == 19690720:
                print(100 * n + v)
                exit(0)
        except IndexError:
            pass
