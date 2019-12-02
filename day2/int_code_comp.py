
# set index
i = 0

# the working data
tape = [1, 0, 0, 3, 99]

# read in first code
a = tape[0]

# read in the instruction codes
b = tape[1]

c = tape[2]

# read in the last code
d = tape[3]

# calculate the new result
if a == 1:
    res = b + c
elif a == 2:
    res = b * c

# store result in tape data
tape[d] = res

### compress this and add start index

# set start index
current_index = 0



if tape[current_index] == 1:
    tape[current_index + 3] = tape[current_index+1] + tape[current_index+2]

elif tape[current_index] == 2:
    tape[current_index + 3] = tape[current_index+1] * tape[current_index+2]

elif tape[current_index] == 99:
    print("we done!")


if tape