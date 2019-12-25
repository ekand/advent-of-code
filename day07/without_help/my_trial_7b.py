from day7.int_code_comp_7b import compute

# Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5):
phases = [9, 8, 7, 6, 5]

program = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
           27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]


# Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6):
phases = [9, 7, 8, 5, 6]
program = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

#


foo = None
tapes = []
for _ in range(5):
    tapes.append(program.copy())
signal = None
for i, tape in enumerate(tapes):
    if i == 0:
        signal, halt = compute(tapes[0], phases[0], 0, True)
        pass
    else:
        signal, halt = compute(tapes[i], phases[i], signal, True)
        pass

round_number = 1
while round_number < 1000:
    for i, tape in enumerate(tapes):
        signal, halt = compute(tapes[i], foo, signal, False)
        print(halt)
        print(signal)
    if halt == "done":
        print("done by halt, signal = ", signal)
        break
    print("end of round. signal:", signal)
    round_number += 1

print("Done!")
print(signal)