from aocd import get_data

# input
f = get_data(day=3, year=2020)


def parse(line: str):
    line = [x == '#' for x in line]
    return line


ls = [parse(line) for line in f.splitlines()]


# part a
def count_trees(slope, lines):
    height = len(lines)
    width = len(lines[0])
    pos = (0, 0)
    hits = 0

    for y in range(0, height):
        # needed to catch overflow by slope steeper than 45degrees
        if pos[1] > height:
            break

        # check if it's a hit
        if lines[pos[1]][pos[0]]:
            hits += 1

        # update position
        pos = pos[0] + slope[0], pos[1] + slope[1]

        # check for horizontal overflow
        if pos[0] >= width:
            pos = pos[0] - width, pos[1]

    return hits


print(count_trees((3, 1), ls))

# part b
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = [count_trees(slope, ls) for slope in slopes]
product = 1
for t in trees:
    product *= t
print(product)
