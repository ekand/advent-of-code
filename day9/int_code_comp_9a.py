def compute(tape, user_input):
    program_input = user_input
    program_output = None
    pointer = 0
    relative_base = 0
    while True:
        instruction = str(tape[pointer ])

        # read in opcode
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
        if opcode == 1:  # add parameters 1 and 2, output to parameter 3
            if modes[0] == 0:
                a = tape[tape[pointer + 1]]
            elif modes[0] == 1:
                a = tape[pointer + 1]
            else:  # modes[0] == 2
                a = tape[tape[pointer + 1 + relative_base]]

            if modes[1] == 0:
                b = tape[tape[pointer + 2]]
            if modes[1] == 1:
                b = tape[pointer + 2]
            if modes[1] == 2:
                b = tape[tape[pointer + 2 + relative_base]]

            c = a + b
            if modes[2] == 0:
                tape[tape[pointer +3]] = c
            elif modes[2] == 1:
                tape[pointer + 3] = c
            else:  # modes[2] == 2
                tape[tape[pointer + 3 + relative_base]] = c

            pointer += 4

        if opcode == 2:  # multiply parameters 1 and 2, output to parameter 3
            if modes[0] == 0:
                a = tape[tape[pointer + 1]]
            elif modes[0] == 1:
                a = tape[pointer + 1]
            else:  # modes[0] == 2
                a = tape[tape[pointer + 1 + relative_base]]

            if modes[1] == 0:
                b = tape[tape[pointer + 2]]
            if modes[1] == 1:
                b = tape[pointer + 2]
            if modes[1] == 2:
                b = tape[tape[pointer + 2 + relative_base]]

            c = a * b
            if modes[2] == 0:
                tape[tape[pointer + 3]] = c
            elif modes[2] == 1:
                tape[pointer + 3] = c
            else:  # modes[2] == 2
                tape[tape[pointer + 3 + relative_base]] = c

            pointer += 4

        # handle opcode 3
        if opcode == 3:  # take int
            if modes[0] == 0:
                tape[tape[pointer + 1]] = program_input
            elif modes[0] == 1:
                tape[pointer + 1] = program_input
            else:  # modes[0] == 2
                tape[pointer + 1 + relative_base] = program_input
            pointer += 2

        # handle opcode 4
        if opcode == 4:  # output int
            if modes[0] == 0:
                program_output = tape[tape[pointer + 1]]
            elif modes[0] == 1:
                program_output = tape[pointer + 1]
            else:
                program_output = tape[tape[pointer + 1 + relative_base]]
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

        if opcode == 9:
            a = tape[tape[pointer]]

        if program_output:
            program_input = program_output
