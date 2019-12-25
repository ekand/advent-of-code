from day7.int_code_comp_7b import compute

# input: tape (program) and initial phases

def feedback_loop(program, phases):
    tapes = []
    for _ in range(5):
        tapes.append(program.copy)
    for i in range(1000):
        if i == 0:
            for tape_number, tape in enumerate(tapes):




