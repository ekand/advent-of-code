import logging
import numpy as np
#
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.debug('This will get logged to a file')
#
# logger = logging.getLogger("this is a logger")
# logger.info("asdf")


with open("input.txt") as file:
    data = [int(x) for x in file.read()]

print(len(data))

layers = []
for i in range(100):
    layers.append([])
    for j in range(150):
        # print(f'i={i}, j= {j}')
        layers[i].append(data[j + 150 * i])


def count_n(layer, n):
    count = 0
    for pixel in layer:
        if pixel == n:
            count += 1
    return count




target_layer_index = 0

foo = np.argmin([count_n(layer, 0) for layer in layers])


result = count_n(layers[foo], 1) * count_n(layers[foo], 2)
print(result)

image = []
for row in range(6):
    for col in range(25):
        pixel = 2
        i = 0
        while pixel == 2:
            pixel = layers[i][col + row * 25]
            i += 1
        image.append(pixel)
        # print(image)

for row in range(25):
    print(image[row * 25: (row + 1)*25])

image_2 = ["*" if x == 1 else " " for x in image]
for row in range(25):
    print(image_2[row * 25: (row + 1)*25])



# answer: CJZLP