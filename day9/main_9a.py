from day9.int_code_comp_9a import compute

with open("input.txt") as file:
    tape_global = [int(s) for s in file.read().split(",")]


#tape_global = [104,1125899906842624,99]

for i in range(10000):
    tape_global.append(0)

foo = compute(tape_global, 1)
print(foo)




