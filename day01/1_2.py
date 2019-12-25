def fuel_needed(mass):
    return mass//3 - 2


def updated_fuel_needed(mass):
    total_fuel = 0
    fuel_n_minus_1 = fuel_needed(mass)
    total_fuel += fuel_n_minus_1
    fuel_n = 1
    while fuel_n > 0:
        fuel_n = fuel_needed(fuel_n_minus_1)
        fuel_n = fuel_n if fuel_n >=0 else 0
        total_fuel += fuel_n
        fuel_n_minus_1 = fuel_n
    return total_fuel




    return additional_fuel


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
    total += updated_fuel_needed(num)
print(total)

print(updated_fuel_needed(1969))