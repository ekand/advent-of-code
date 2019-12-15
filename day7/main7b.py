from day7.int_code_comp_7b import compute
from itertools import permutations

# with open("input.txt") as file:
#     tape = [int(x) for x in file.read().split(",")]

tape = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]



# phases = [5, 6, 7, 8, 9]
# test_phases = permutations(phases)
test_phases =[ [9,7,8,5,6]]

max_output_signal = 0
for set_of_phases in test_phases:
    tape_A = tape.copy()
    tape_B = tape.copy()
    tape_C = tape.copy()
    tape_D = tape.copy()
    tape_E = tape.copy()
    tapes = [tape_A, tape_B, tape_C, tape_D, tape_E]
    input_signal = 0
    j = 0
    while j < 50:
        i = 0
        for i, local_tape in enumerate(tapes):
            if j == 0:
                input_signal = compute(local_tape, set_of_phases[i], input_signal)

            else:
                print(input_signal)
                input_signal = compute(local_tape, input_signal, input_signal)

            print(input_signal, j, i)
        j += 1


