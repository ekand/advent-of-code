import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)


with open("toy_input_part_b.txt", "r") as file:
    orbit_map = [(string[0:3], string[4:]) for string in file.read().split('\n')]


counter_global = 0
num_orbital_transfers_needed = None


def search_upstream(planet, depth):
    logging.debug(f"search_upstream(): checking planet {planet} with depth {depth}")
    global num_orbital_transfers_needed
    if num_orbital_transfers_needed:
        return


    # get upstream planet
    for edge in orbit_map:
        if edge[1] == planet:
            new_planet = edge[0]

            # look downstream from new planet
            search_downstream(new_planet, depth + 1)

            # search upstream from new planet
            search_upstream(new_planet, depth + 1)


def search_downstream(planet, depth):
    logging.debug(f"search_downstream(): checking planet {planet} with depth {depth}")
    global num_orbital_transfers_needed
    if num_orbital_transfers_needed:
        return

    for edge in orbit_map:
        if edge[0] == planet:
            new_planet = edge[1]
            if new_planet == 'SAN':
                num_orbital_transfers_needed = depth

            search_downstream(new_planet, depth + 1)


search_upstream("YOU", -1)
print(num_orbital_transfers_needed)

logging.debug("\n")

# orbit_checksum("COM")
# print(counter_global)

