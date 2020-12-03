import itertools

from aocd import get_data

# input
f = get_data(day=2, year=2020)
lines = [line for line in f.splitlines()]

# part a
res_a = 0
for line in lines:
    (a, char, password) = line.split(" ")
    char = char.split(':')[0]
    a, z = [int(x) for x in a.split("-")]

    count = password.count(char)
    if a <= count <= z:
        res_a += 1
print(res_a)

# part b
res_b = 0
for line in lines:
    (a, char, password) = line.split(" ")
    char = char.split(':')[0]
    a, z = [int(x) for x in a.split("-")]

    a = password[a - 1]
    z = password[z - 1]
    if (a == char and z != char) or (a != char and z == char):
        res_b += 1
print(res_b)
