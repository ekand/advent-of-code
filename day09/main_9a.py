from day9.int_code_comp_9a import compute

with open("input.txt") as file:
    tape_global = [int(s) for s in file.read().split(",")]


# tape_global = [104,1125899906842624,99]
# tape_global = [1102,34915192,34915192,7,4,7,99,0]
# tape_global = [109,19, 204, -34]
# tape_global = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# tape_global = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99 ]
tape_global = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

for i in range(10000):
    tape_global.append(0)

foo = compute(tape_global, 1)
print(foo)



