'''
https://adventofcode.com/2019/day/2

Usage: cat day5input.txt | python3 day5part2.py
'''


INP = 5


prog = list(map(int, input().split(',')))


opcode_num_parms = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    99: 0,
}


def get_opcode_modes(opcm):
    opcode = opcm % 100
    num_parms = opcode_num_parms[opcode]
    opcm //= 100
    modes = []
    while opcm > 0:
        modes.append(opcm % 10)
        opcm //= 10
    modes += [0] * (num_parms - len(modes))
    return opcode, modes


ip = 0
while ip < len(prog):
    opcm = prog[ip]
    opcode, modes = get_opcode_modes(opcm)
    if opcode == 1:
        n1 = prog[ip + 1] if modes[0] == 1 else prog[prog[ip + 1]]
        n2 = prog[ip + 2] if modes[1] == 1 else prog[prog[ip + 2]]
        prog[prog[ip + 3]] = n1 + n2
    elif opcode == 2:
        n1 = prog[ip + 1] if modes[0] == 1 else prog[prog[ip + 1]]
        n2 = prog[ip + 2] if modes[1] == 1 else prog[prog[ip + 2]]
        prog[prog[ip + 3]] = n1 * n2
    elif opcode == 3:
        prog[prog[ip + 1]] = INP
    elif opcode == 4:
        print(prog[ip + 1] if modes[0] == 1 else prog[prog[ip + 1]])
    elif opcode == 5:
        n = prog[ip + 1] if modes[0] == 1 else prog[prog[ip + 1]]
        if n != 0:
            ip = prog[ip + 2] if modes[1] == 1 else prog[prog[ip + 2]]
            continue
    elif opcode == 6:
        n = prog[ip + 1] if modes[0] == 1 else prog[prog[ip + 1]]
        if n == 0:
            ip = prog[ip + 2] if modes[1] == 1 else prog[prog[ip + 2]]
            continue
    elif opcode == 7:
        n1 = prog[ip + 1] if modes[0] == 1 else prog[prog[ip + 1]]
        n2 = prog[ip + 2] if modes[1] == 1 else prog[prog[ip + 2]]
        prog[prog[ip + 3]] = 1 if n1 < n2 else 0
    elif opcode == 8:
        n1 = prog[ip + 1] if modes[0] == 1 else prog[prog[ip + 1]]
        n2 = prog[ip + 2] if modes[1] == 1 else prog[prog[ip + 2]]
        prog[prog[ip + 3]] = 1 if n1 == n2 else 0
    else:
        break
    ip += opcode_num_parms[opcode] + 1
