from typing import List

Program = List[int]   # typing of Program

def run(program: Program) -> None:
    pos = 0

    while program[pos] != 99: # halt
        opcode, loc1, loc2, loc3 = program[pos], program[pos + 1], program[pos + 2], program[pos + 3]   # tuple unpacking
        if opcode == 1:
            program[loc3] = program[loc1] + program[loc2]
        elif opcode == 2:
            program[loc3] = program[loc1] * program[loc2]
        else:
            raise RuntimeError(f"invalid opcode: {program[pos]}")

        pos += 4

prog1 = [1,0,0,0,99]; run(prog1); assert prog1 == [2,0,0,0,99]
print('done')


        