import re


def in_range(number):
    return 130254 < number < 678275


def non_decreasing(number):
    prev = -1
    for character in str(number):
        if int(character) < prev:
            return False
        prev = int(character)
    return True


def has_adjacent_digits(number):
    return bool(re.search(r'(\d)\1+', str(number)))


def has_strictly_two_adjacent_digits(number):
    iterator = re.finditer(r'(\d)\1+', str(number))
    for match in iterator:
        if len(match.group()) == 2:
            return True
    return False


def test_num_part_2 (num):
    return non_decreasing(num) and has_strictly_two_adjacent_digits(num) and len(str(num)) == 6



def test_num(num):
    return non_decreasing(num) and has_adjacent_digits(num) and len(str(num)) == 6


count = 0
for number in range(130254, 678275):
    if test_num(number):
        count += 1

print('part 1', count)

count = 0
for number in range(130254, 678275):
    if test_num_part_2(number):
        count += 1
print('part 2', count)






