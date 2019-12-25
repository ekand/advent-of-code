# adapted (well, copied with comments added) from Joel Grus's solution on GitHub

from enum import Enum
from typing import List, Tuple
from collections import deque

class Opcode(Enum):
    ADD = 1
    MULTIPLY = 2
    STORE_INPUT = 3
    SEND_TO_OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    END_PROGRAM = 99


Modes = List[int]


def parse_opcode(opcode_full: int, num_modes: int = 3) -> Tuple[Opcode, Modes]:
    opcode_part = opcode_full % 100  # comment first two digits from right to left

    modes: List[int] = []
    opcode_full = opcode_full // 100   # oh wait, that throws away the right two digits (which we already used)

    for _ in range(num_modes):
        modes.append(opcode_full % 10) # the next one number from right to left
        opcode_full = opcode_full // 10

    return Opcode(opcode_part), modes  # Opcode(opcode_part) seems to be using the variables in Opcode class.

Program = List[int]  # typing program

class Amplifier:
    def __init__(self, program: List[int], phase: int) -> None:
        self.program = program[:]  # make a copy of program
        self.inputs = deque([phase])  # make a double ended queue of phase
        self.pos = 0

    def get_value(self, pos: int, mode: int) -> int:
        if mode == 0:
            # pointer mode
            return self.program[self.program[pos]] # it's a really good idea to package this as a function. In my version I ended up writing it a whole bunch of times
        elif mode == 1:
            # immediate mode
            return self.program[pos]
        else:
            raise ValueError(f"unknown mode: {mode}")

    def step(self, input_value: int) -> int:
        self.inputs.append(input_value)  # inputs is a double ended queue from the class definition

        while True:
            opcode, modes = parse_opcode(self.program[self.pos])  # read in an instruction from the program
            
            if opcode == Opcode.END_PROGRAM:
                return None  # apparently Joel thinks there's something sub-optimal about this, but I'm not sure what it was...
            elif opcode == Opcode.ADD:
                value1 = self.get_value(self.pos + 1, modes[0])
                value2 = self.get_value(self.pos + 2, modes[1])
                self.program[self.program[self.pos + 3]] = value1 + value2  # apparently this is always in position mode ?
                self.pos += 4
            elif opcode == Opcode.MULTIPLY:
                value1 = self.get_value(self.pos + 1, modes[0])
                value2 = self.get_value(self.pos + 2, modes[1])
                self.program[self.program[self.pos + 3]] = value1 * value2
                self.pos += 4
            elif opcode == Opcode.STORE_INPUT:
                # get input and store at location
                loc = self.program[self.pos + 1]  # why doesn't it need to consider mode here?
                input_value = self.inputs.popleft()  # why do we need a queue here, and not just a single variable?
                self.program[loc] = input_value
                self.pos += 2
            elif opcode == Opcode.SEND_TO_OUTPUT:
                # get value from location
                value = self.get_value(self.pos + 1, modes[0])
                self.pos += 2
                return value

            elif opcode == Opcode.JUMP_IF_TRUE:   # jump if truthy. (?)
                value1 = self.get_value(self.pos + 1, modes[0])
                value2 = self.get_value(self.pos + 2, modes[1])

                if value1 != 0:
                    self.pos = value2   # jump!
                else:
                    self.pos += 3    # move to next instruction/full opcode
                
            elif opcode == Opcode.LESS_THAN:
                value1 = self.get_value(self.pos + 1, modes[0])
                value2 = self.get_value(self.pos + 2, modes[1])

                if value1 < value2:
                    self.program[self.program[self.pos + 3]] = 1  # again apparently in position mode always?
                else:
                    self.program[self.program[self.pos + 3]] = 0
                self.pos += 4

            elif opcode == Opcode.EQUALS:
                value1 = self.get_value(self.pos + 1, modes[0])
                value2 = self.get_value(self.pos + 2, modes[1])

                if value1 == value2:
                    self.program[self.program[self.pos + 3]] = 1
                else:
                    self.program[self.program[self.pos + 3]] = 0
                self.pos += 4

            else:
                raise RuntimeError(f"invaled opcode: {opcode}")  # #fup why raise and not... something else I don't quite recall

def run_amplifiers(program: List[int], phases: List[int]) -> int:
    amplifiers = [Amplifier( program, phase) for phase in phases]
    n = len(amplifiers)
    num_finished = 0

    last_output = 0
    last_non_none_output = None
    ampid = 0

    while num_finished < n:
        last_output = amplifiers[ampid].step(last_output)
        if last_output is None:
            num_finished += 1
        else:
            last_non_none_output = last_output
        ampid = (ampid + 1) % n  #  move on to next amplifier (stepping back to first on if needed)
    
    return last_non_none_output


PROG1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
PHASES1 = [9,8,7,6,5]
assert run_amplifiers(PROG1, PHASES1) == 139629729

