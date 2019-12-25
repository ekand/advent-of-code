with open('input.txt') as file:
    file_contents = file.read()
    # print(file_contents)
    data = file_contents.split("\n")
    wire_a_directions, wire_b_directions, _ = data
    # print(wire_a_directions)
    # print(wire_b_directions)
    wire_a_directions = wire_a_directions.split(",")
    wire_b_directions = wire_b_directions.split(",")
# print(wire_a_directions)
# print(wire_b_directions)


directions_x_dict = {'U': 0, 'D': 0, 'R': 1, 'L': -1}
directions_y_dict = {'U': 1, 'D': -1, 'R': 0, 'L': 0}


def get_points(wire_instructions):
    x, y = 0, 0
    points_set = set()
    for cmd in wire_instructions:
        direction = cmd[0]
        distance = int(cmd[1:])
        assert direction in directions_x_dict 
        assert direction in directions_y_dict
        for step in range(distance):
            x += directions_x_dict[direction]
            y += directions_y_dict[direction]
            points_set.add((x, y))
    return points_set
a_points_set = get_points(wire_a_directions)
b_points_set  = get_points(wire_b_directions)
a_b_points_set_union = a_points_set & b_points_set
# print(a_b_points_set_union)
# print(points_set)
distances = [abs(x)+abs(y) for (x, y) in a_b_points_set_union]
print(min(distances))
