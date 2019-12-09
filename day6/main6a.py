with open("input.txt", "r") as file:
    orbit_map = [(string[0:3], string[4:]) for string in file.read().split('\n')]


def orbit_checksum(planet, depth=1):
    global counter_global
    for edge in orbit_map:
        if edge[0] == planet:
            counter_global += depth
            orbit_checksum(edge[1], depth + 1)
    return


counter_global = 0
print(orbit_checksum("COM"))
print(counter_global)
