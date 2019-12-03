'''
https://adventofcode.com/2019/day/1

Usage: cat day1part2input.txt | python3 day1part2.py
'''


import sys


fuel = 0
for mass in sys.stdin:
    mass = int(mass)
    added_fuel = max(mass // 3 - 2, 0)
    while added_fuel > 0:
        fuel += added_fuel
        added_fuel = max(added_fuel // 3 - 2, 0)
print(fuel)
