def compute(tape):
    current_index = 0
    while True:
        tape_at_current_index = tape[current_index]
        if tape_at_current_index == 99:
            print('time to break')
            break
        elif tape[current_index] == 1:
            tape[tape[current_index + 3]] = tape[tape[current_index + 1]] + tape[tape[current_index + 2]]
        elif tape[current_index] == 2:
            tape[tape[current_index + 3]] = tape[tape[current_index + 1]] * tape[tape[current_index + 2]]
        current_index += 4
    return tape

