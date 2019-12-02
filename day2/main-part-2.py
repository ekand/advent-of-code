from day2.int_code_comp import compute
# let's just go brute force here

with open("input.txt") as file:
    data = file.read()
    data = data.strip().split(",")
    tape = []
    for string in data:
        tape.append(int(string))

result = None
for noun in range(100):
    for verb in range(100):
        print("noun", noun, "verb", verb)
        new_tape = tape[:]
        new_tape[1] = noun
        new_tape[2] = verb
        computed_new_tape_result = None
        try:
            computed_new_tape_result = compute(new_tape)[0]
            pass
        except IndexError:
            print("exception")
            continue
        if computed_new_tape_result == 19690720:
            result = (noun, verb)
            print("yes!")
        else:
            print("no")

print("result", result)
print(result[0]*100 + result[1])