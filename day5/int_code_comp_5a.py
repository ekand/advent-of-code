def compute(tape, user_input):
    program_input = user_input
    i = 0
    while True:
        instruction = str(tape[i])
        opcode = int(instruction[-2:])
        # check for halt code
        if opcode == 99:
            break

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
            a = tape[tape[i + 1]] if modes[0] == 0 else tape[i + 1]
            b = tape[tape[i + 2]] if modes[1] == 0 else tape[i + 2]
            c = a + b
            if modes[2] == 0:
                tape[tape[i+3]] = c
            else:
                tape[i+3] = c
            i += 4

        # handle opcode 2 (Should be identical to opcode 1 except that it multiplies
        if opcode == 2:
            a = tape[tape[i + 1]] if modes[0] == 0 else tape[i + 1]
            b = tape[tape[i + 2]] if modes[1] == 0 else tape[i + 2]
            c = A * B
            if modes[2] == 0:
                tape[tape[i + 3]] = c
            else:
                tape[i + 3] = c
            i += 4

        # handle opcode 3
        # todo what is input and output for this?
        if opcode == 3:
            if modes[0] == 0:
                tape[tape[i+1]] = program_input
            else:
                tape[i+1] = program_input

        if opcode == 4:
            program_input = tape[tape[i+1]]


            i += 2
        program_input = program_output
        break
