def compute(tape, user_input):
    program_input = user_input
    program_output = None
    pointer = 0
    while True:
        instruction = str(tape[pointer ])

        #read in opcode
        opcode = int(instruction[-2:])

        # check for halt code
        if opcode == 99:
            return program_output

        # read in modes
        modes = [0, 0, 0]
        try:
            modes[0] = int(instruction[-3])
            pass
        except IndexError:
            modes[0] = 0
        try:
            modes[1] = int(instruction[-4])
        except IndexError:
            modes[1] = 0
        try:
            modes[2] = int(instruction[-5])
        except IndexError:
            modes[2] = 0

        # handle opcode 1
        # opcode = 1
        if opcode == 1:
            a = tape[tape[pointer + 1]] if modes[0] == 0 else tape[pointer + 1]
            b = tape[tape[pointer + 2]] if modes[1] == 0 else tape[pointer + 2]
            c = a + b
            if modes[2] == 0:
                tape[tape[pointer +3]] = c
            else:
                tape[pointer +3] = c
            pointer += 4

        # handle opcode 2 (Should be identical to opcode 1 except that it multiplies
        if opcode == 2:
            a = tape[tape[pointer + 1]] if modes[0] == 0 else tape[pointer + 1]
            b = tape[tape[pointer + 2]] if modes[1] == 0 else tape[pointer + 2]
            c = a * b
            if modes[2] == 0:
                tape[tape[pointer + 3]] = c
            else:
                tape[pointer + 3] = c
            pointer += 4

        # handle opcode 3
        if opcode == 3:
            if modes[0] == 0:
                tape[tape[pointer + 1]] = program_input
            else:
                tape[pointer +1] = program_input
            pointer += 2

        # handle opcode 4
        if opcode == 4:
            if modes[0] == 0:
                program_output = tape[tape[pointer + 1]]
            else:
                program_output = tape[pointer + 1]
            pointer += 2

        if opcode == 5:  # jump if true
            if modes[0] == 0:
                if tape[tape[pointer + 1]] != 0:
                    pointer = tape[tape[pointer + 2]] if modes[1] == 0 else tape[pointer + 2]
                else:
                    pointer += 3;
            else: # modes[0] = 1
                if tape[pointer + 1] != 0:
                    pointer = tape[tape[pointer + 2]] if modes[1] == 0 else tape[pointer + 2]
                else:
                    pointer += 3;

        if opcode == 6:  # jump if false
            if modes[0] == 0:
                if tape[tape[pointer + 1]] == 0:
                    pointer = tape[tape[pointer + 2]] if modes[1] == 0 else tape[pointer + 2]
                else:
                    pointer += 3;
            else: # modes[0] = 1
                if tape[pointer + 1] == 0:
                    pointer = tape[tape[pointer + 2]] if modes[1] == 0 else tape[pointer + 2]
                else:
                    pointer += 3;

        if opcode == 7:
            a = tape[tape[pointer + 1]] if modes[0] == 0 else tape[pointer + 1]
            b = tape[tape[pointer + 2]] if modes[1] == 0 else tape[pointer + 2]
            comparison_result = 1 if a < b else 0
            if modes[2] == 0:
                tape[tape[pointer + 3]] = comparison_result
            else:
                tape[pointer + 3] = comparison_result
            pointer += 4

        if opcode == 8:
            a = tape[tape[pointer + 1]] if modes[0] == 0 else tape[pointer + 1]
            b = tape[tape[pointer + 2]] if modes[1] == 0 else tape[pointer + 2]
            comparison_result = 1 if a == b else 0
            if modes[2] == 0:
                tape[tape[pointer + 3]] = comparison_result
            else:
                tape[pointer + 3] = comparison_result
            pointer += 4

        if program_output:
            program_input = program_output
