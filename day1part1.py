'''
https://adventofcode.com/2019/day/1

Usage: cat day1part1input.txt | python3 day1part1.py
'''


import sys


fuel = 0
for mass in sys.stdin:
    mass = int(mass)
    fuel += max(mass // 3 - 2, 0)
print(fuel)
