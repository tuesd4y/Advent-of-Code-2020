from aocd import get_data
import numpy as np

# input
f = get_data(day=5, year=2020)


def parse(line: str):
    row = line[:7]
    col = line[7:]

    row = [(x == 'B') * 2**(6-i) for i, x in enumerate(row)]
    col = [(x == 'R') * 2**(2-i) for i, x in enumerate(col)]

    return np.sum(row), np.sum(col)


lines = [parse(line) for line in f.splitlines()]


# part a
ids = [row * 8 + col for row, col in lines]
print(np.max(ids))


def exists(i):
    # part b
    return i-1 in ids and i+1 in ids


for i in range(0,np.max(ids)+1):
    if not exists(i):
        print(i)
