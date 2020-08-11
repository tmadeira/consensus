# A graph is represented by a pair of arrays `(e, w)` where `e` is an adjacency
# list and `w[i][j]` is the weight of the edge `(i, e[i][j])`.

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
