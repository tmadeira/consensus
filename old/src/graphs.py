# A graph is represented by a pair of arrays `(e, w)` where `e` is an adjacency
# list and `w[i][j]` is the weight of the edge `(i, e[i][j])`.

import math

def make_cycle(n):
    e = []
    w = []
    for i in range(n):
        e.append([(i+n-1) % n, (i+n+1) % n])
        w.append([.5, .5])
    return (e, w)

def make_path(n):
    e = [[1]]
    w = [[1]]
    for i in range(1, n-1):
        e.append([(i+n-1) % n, (i+n+1) % n])
        w.append([.5, .5])
    e.append([n-2])
    w.append([1])
    return (e, w)

def make_complete(n):
    e = []
    w = []
    for i in range(n):
        e.append([])
        w.append([])
        for j in range(n):
            if j == i:
                continue
            e[i].append(j)
            w[i].append(1.0 / (n-1))
    return (e, w)

def make_gridcycle(n):
    m = int(math.sqrt(n) + 0.5)
    if m ** 2 != n:
        raise Exception("n must be a perfect square to generate a gridcycle")

    def grid_id(x, y):
        return (x % m) * m + (y % m)

    e = []
    w = []
    for i in range(n):
        e.append([])
        w.append([])

        x = i // m
        y = i % m
        for j in [grid_id(x-1, y), grid_id(x, y-1), grid_id(x+1, y), grid_id(x, y+1)]:
            e[i].append(j)
            w[i].append(0.25)

    return (e, w)

def make_expandedcycle(n):
    m = int(math.sqrt(n) + 0.5)
    if m ** 2 != n:
        raise Exception("n must be a perfect square to generate a expandedcycle")

    e = []
    w = []
    for i in range(n):
        e.append([])
        w.append([])

        start = (i // m) * m
        end = start + m

        weight = 1.0 / (m-1)
        if i == start:
            weight = 1.0 / (m+1)
            e[i].append((i-m) % n)
            w[i].append(weight)
            e[i].append((i+m) % n)
            w[i].append(weight)

        for j in range(start, end):
            if i == j:
                continue
            e[i].append(j)
            w[i].append(weight)

    return (e, w)
