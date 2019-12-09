from day5.int_code_comp_5b import compute

with open("input5.txt", "r") as file:
    tape = [int(s) for s in file.read().split(",")]
pass

foo = compute(tape, 5)
print(foo)

# bar = compute([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], -6)
# print(bar)
