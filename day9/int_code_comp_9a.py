import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)

def compute(tape, user_input):
    program_output = None
    program_input = user_input
    logging.debug(f"program input {program_input}, program_output {program_output}  ")


    pointer = 0
    relative_base = 0
    while True:

        instruction = str(tape[pointer])

        # read in opcode
        opcode = int(instruction[-2:])


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

        logging.debug(f"pointer {pointer}, program memory: {tape[pointer:pointer+5]}, relative_base {relative_base}, program input {program_input}, program_output {program_output}, opcode {opcode}, modes {modes}")

        # check for halt code
        if opcode == 99:
            logging.debug("program halting. \n")
            return program_output

        # ============================ #
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
                tape[tape[pointer + 3]] = c
            elif modes[2] == 1:
                tape[pointer + 3] = c
            else:  # modes[2] == 2
                tape[tape[pointer + 3 + relative_base]] = c

            pointer += 4

        # ============================ #
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

        # ============================ #
        if opcode == 3:  # take int
            if modes[0] == 0:
                tape[tape[pointer + 1]] = program_input
            elif modes[0] == 1:
                tape[pointer + 1] = program_input
            else:  # modes[0] == 2
                tape[pointer + 1 + relative_base] = program_input
            pointer += 2

        # ============================ #
        if opcode == 4:  # output int
            if modes[0] == 0:
                program_output = tape[tape[pointer + 1]]
            elif modes[0] == 1:
                program_output = tape[pointer + 1]
            else:
                program_output = tape[tape[pointer + 1 + relative_base]]
            pointer += 2

        # ============================ #
        if opcode == 5:  # jump if true
            if modes[0] == 0:
                a = tape[tape[pointer + 2]]
            elif modes[0] == 1:
                a = tape[pointer + 2]
            else:  # modes[0] == 2:
                a = tape[pointer + 2 + relative_base]

            if a != 0:
                if modes[1] == 0:
                    pointer = tape[tape[pointer + 2]]
                elif modes[1] == 1:
                    pointer = tape[pointer + 2]
                else:  # modes[1] == 2
                    pointer = tape[tape[pointer + 2 + relative_base]]
            else:
                pointer += 3

        # ============================ #
        if opcode == 6:  # jump if false
            if modes[0] == 0:
                a = tape[tape[pointer + 2]]
            elif modes[0] == 1:
                a = tape[pointer + 2]
            else:  # modes[0] == 2:
                a = tape[pointer + 2 + relative_base]

            if a == 0:
                if modes[1] == 0:
                    pointer = tape[tape[pointer + 2]]
                elif modes[1] == 1:
                    pointer = tape[pointer + 2]
                else:  # modes[1] == 2
                    pointer = tape[tape[pointer + 2 + relative_base]]
            else:
                pointer += 3

        # ============================ #
        if opcode == 7:  # less than
            if modes[0] == 0:
                a = tape[tape[pointer + 1]]
            elif modes[0] == 1:
                a = tape[pointer + 1]
            else:  # modes[0] == 2
                a = tape[tape[pointer + 1 + relative_base]]

            if modes[1] == 0:
                b = tape[tape[pointer + 1]]
            elif modes[1] == 1:
                b = tape[pointer + 1]
            else:  # modes[1] == 2
                b = tape[tape[pointer + 1 + relative_base]]

            comparison_result = 1 if a < b else 0
            if modes[2] == 0:
                tape[tape[pointer + 3]] = comparison_result
            elif modes[2] == 1:
                tape[pointer + 3] = comparison_result
            else:  # modes [2] == 2
                tape[tape[pointer + 3]] = comparison_result
            pointer += 4

        # ============================ #
        if opcode == 8: # greater than
            if modes[0] == 0:
                a = tape[tape[pointer + 1]]
            elif modes[0] == 1:
                a = tape[pointer + 1]
            else:  # modes[0] == 2
                a = tape[tape[pointer + 1 + relative_base]]

            if modes[1] == 0:
                b = tape[tape[pointer + 1]]
            elif modes[1] == 1:
                b = tape[pointer + 1]
            else:  # modes[1] == 2
                b = tape[tape[pointer + 1 + relative_base]]

            comparison_result = 1 if a < b else 0
            if modes[2] == 0:
                tape[tape[pointer + 3]] = comparison_result
            elif modes[2] == 1:
                tape[pointer + 3] = comparison_result
            else:  # modes [2] == 2
                tape[tape[pointer + 3]] = comparison_result
            pointer += 4

        # ============================ #
        if opcode == 9:  # adjust relative_base
            if modes[0] == 0:
                x = tape[tape[pointer + 1]]
            elif modes[0] == 1:
                x = tape[pointer + 1]
            else:  # modes[0] == 2
                x = tape[tape[pointer + 1 + relative_base]]
            relative_base += x
            pointer += 2

        # ============================ #
        if program_output:
            program_input = program_output
