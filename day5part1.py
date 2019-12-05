'''
https://adventofcode.com/2019/day/2

Usage: cat day5input.txt | python3 day5part1.py
'''


INP = 1


prog = list(map(int, input().split(',')))


def get_opcode_modes(opcm):
    opcode = opcm % 100
    opcode_num_parms = {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        99: 0,
    }
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
        ip += 4
    elif opcode == 2:
        n1 = prog[ip + 1] if modes[0] == 1 else prog[prog[ip + 1]]
        n2 = prog[ip + 2] if modes[1] == 1 else prog[prog[ip + 2]]
        prog[prog[ip + 3]] = n1 * n2
        ip += 4
    elif opcode == 3:
        prog[prog[ip + 1]] = INP
        ip += 2
    elif opcode == 4:
        print(prog[ip + 1] if modes[0] == 1 else prog[prog[ip + 1]])
        ip += 2
    else:
        break
