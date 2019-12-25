from day7.int_code_comp_7a import compute
from itertools import permutations

with open("input.txt") as file:
    tape = [int(x) for x in file.read().split(",")]

phases = [3, 4, 2, 1, 0]
test_phases = permutations(phases)

max_output_signal = 0
for set_of_phases in test_phases:
    input_signal = 0
    for phase in set_of_phases:
        local_tape = tape.copy()
        input_signal = compute(local_tape, phase, input_signal)
    output_signal = input_signal
    if output_signal > max_output_signal:
        max_output_signal = output_signal
        max_phases = set_of_phases


print(max_phases)
print(max_output_signal)

# the answer was 929800
