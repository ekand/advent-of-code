import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)


with open("toy_input_part_b.txt", "r") as file:
    orbit_map = [(string[0:3], string[4:]) for string in file.read().split('\n')]

you_found = False
san_found = False
counter_global = 0


def orbit_checksum(planet, depth=1):
    logging.debug(f"checking planet {planet}")
    global counter_global
    global you_found
    global san_found

    if planet == 'YOU':
        you_found = True
        print("found you")
    if planet == "SAN":
        san_found = True
        print("found santa")

    if you_found and san_found:
        print("hooray!")
    for edge in orbit_map:
        if edge[0] == planet:
            counter_global += depth
            orbit_checksum(edge[1], depth + 1)
    return


orbit_checksum("COM")
print(counter_global)

