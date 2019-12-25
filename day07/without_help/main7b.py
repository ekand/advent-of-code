from day7.int_code_comp_7b import compute
from itertools import permutations

with open("input.txt") as file:
    tape = [int(x) for x in file.read().split(",")]

# phases = [3, 4, 2, 1, 0]
# test_phases = permutations(phases)
#
# max_output_signal = 0
# for set_of_phases in test_phases:
#     input_signal = 0
#     for phase in set_of_phases:
#         local_tape = tape.copy()
#         input_signal = compute(local_tape, phase, input_signal)
#     output_signal = input_signal
#     if output_signal > max_output_signal:
#         max_output_signal = output_signal
#         max_phases = set_of_phases
#
# print(max_phases)
# print(max_output_signal)
#
# # the answer was 929800
#

# Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5):

test_program = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
                -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
                53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]
phases = [9, 8, 7, 6, 5]
test_phases = [phases]
# test_phases = permutations(phases)

# tape = test_program

tapes = []
for _ in range(5):
    tapes.append(tape.copy())

done = False
first_round = True
second_round = True
last_round = False
input_signal = 0
while not done:
    if first_round:
        for i, tape in enumerate(tapes):
            my_output, done = compute(tape, phases[i])
        first_round = False
        print("first_round_done")
    elif second_round:
        tape = tapes[0]
        my_output, done = compute(tape, 0)
        for i, tape in enumerate(tapes):
            if i:
                my_output, done = compute(tape, my_output)
        second_round = False
        print("second_round_done")
    elif not last_round:
        for i, tape in enumerate(tapes):
            my_output, done = compute(tape, my_output)
        print("another round done")
        print(my_output)
        if done:
            print("all done")
            break
print(my_output)
