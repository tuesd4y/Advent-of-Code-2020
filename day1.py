import itertools

from aocd import get_data

# input
f = get_data(day=1, year=2020)
ns = [int(line) for line in f.splitlines()]

# part a
# iterate over all 2-combinations of numbers
res_a = 0
for a, b in itertools.combinations(ns, 2):
    if a + b == 2020:
        res_a = a * b

print(res_a)

# iterate over all 3-combinations of numbers
res_b = 0
for a, b, c in itertools.combinations(ns, 3):
    if a + b + c == 2020:
        res_b = a * b * c

print(res_b)
