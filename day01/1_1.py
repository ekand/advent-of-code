def fuel_needed(mass):
    return mass//3 - 2


with open("input2.txt", 'r') as file:
    numbers = []
    while True:
        data = file.readline()
        if data:
            numbers.append(int(data.strip()))
        if not data:
            break

total = 0
for num in numbers:
    total += fuel_needed(num)
print(total)

print(fuel_needed(12))