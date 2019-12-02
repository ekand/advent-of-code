
tape = [1,2,0, 2, 99]
def compute(tape):
    current_index = 0
    while True:
        print(tape)

        if tape[current_index] == 1:
            tape[tape[current_index + 3]] = tape[tape[current_index + 1]] + tape[tape[current_index + 2]]
        elif tape[current_index] == 2:
            tape[tape[current_index + 3]] = tape[tape[current_index + 1]] * tape[tape[current_index + 2]]
        elif tape[current_index] == 99:
            break
        current_index += 4
    return tape

# the working data

