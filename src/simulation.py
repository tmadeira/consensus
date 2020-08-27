import copy
import numpy as np
import graphs

def add_memory(e, w, labels, memory):
    e = copy.deepcopy(e)
    w = copy.deepcopy(w)
    labels = np.copy(labels)

    n = len(e)
    labels = np.tile(labels, len(memory))

    for u in range(n):
        m = len(e[u])
        for i in range(m, m * len(memory)):
            e[u].append(e[u][i-m] + n)
            w[u].append(w[u][i-m])
        w[u] = w[u] * np.repeat(memory, m)

    return (e, w, labels)

def run(n, colors=2, times=200, seed=0, memory=[1.0], tp="cycle", init=[], ID='#', rand_init=False, quiet=False):
    rand = np.random.RandomState(seed)

    # Make graph.
    if tp == "cycle":
        (ee, ww) = graphs.make_cycle(n)
    elif tp == "path":
        (ee, ww) = graphs.make_path(n)
    elif tp == "complete":
        (ee, ww) = graphs.make_complete(n)
    elif tp == "gridcycle":
        (ee, ww) = graphs.make_gridcycle(n)
    elif tp == "expandedcycle":
        (ee, ww) = graphs.make_expandedcycle(n)
    else:
        raise Exception("unknown type")

    # Set initial labels.
    if rand_init:
        pass
    elif len(init) > 0:
        init = np.array(init)
    else:
        init = rand.randint(0, colors, size=n)

    if not rand_init:
        # Add memory.
        (e, w, initial_labels) = add_memory(ee, ww, initial_labels, memory)

    # Run simulation.
    counts = []
    for t in range(times):
        if rand_init:
            labels = rand.randint(0, colors, size=n)

            # Add memory.
            (e, w, labels) = add_memory(ee, ww, labels, memory)
        else:
            labels = init

        count = 0
        while not np.all(labels == labels[0]):
            next_labels = np.empty(len(labels))
            for i in range(n):
                next_labels[i] = labels[rand.choice(e[i], p=w[i])]
            for i in range(n, len(labels)):
                next_labels[i] = labels[i-n]
            labels = next_labels
            count += 1

        counts.append(count)

    if not quiet:
        print(ID, np.mean(counts), np.std(counts), flush=True)

    return [np.mean(counts), np.std(counts), np.median(counts), counts]
