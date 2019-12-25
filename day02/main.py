from int_code_comp import compute

with open("input-edit.txt") as file:  # input-edit.txt has been edited with the input 12, 2 from the problem
    data = file.read()
    data = data.strip().split(",")
    tape = []
    for string in data:
        tape.append(int(string))

tape = compute(tape)
print(tape)

