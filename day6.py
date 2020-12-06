from typing import List

from aocd import get_data
import numpy as np

# input
f = get_data(day=6, year=2020)


def parse(lines: str) -> np.ndarray:
    l: List[str] = lines.splitlines()
    arr: np.ndarray = np.zeros((len(l), 26))
    for index, p in enumerate(l):
        for c in p:
            arr[index, ord(c) - ord('a')] = True

    return arr


groups = [parse(group) for group in f.split('\n\n')]

# part a
print(np.sum([np.sum(np.any(g, axis=0)) for g in groups]))
# part b
print(np.sum([np.sum(np.all(g, axis=0)) for g in groups]))
