from day2.int_code_comp import compute

with open("input-edit.txt") as file:
    data = file.read()
    data = data.strip().split(",")
    tape = []
    for string in data:
        tape.append(int(string))

tape = compute(tape)
print(tape)

