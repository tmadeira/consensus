import numpy as np
import graphs

def add_memory(e, w, labels, memory):
    n = len(e)
    labels = np.tile(labels, len(memory))

    for u in range(n):
        m = len(e[u])
        for i in range(m, m * len(memory)):
            e[u].append(e[u][i-m] + n)
            w[u].append(w[u][i-m])
        w[u] = w[u] * np.repeat(memory, m)

    return (e, w, labels)

def run(n, colors=2, times=200, seed=0, memory=[1.0], tp="cycle", init=[], ID='#'):
    np.random.seed(seed)

    # Make graph.
    if tp == "cycle":
        (e, w) = graphs.make_cycle(n)
    elif tp == "path":
        (e, w) = graphs.make_path(n)
    elif tp == "complete":
        (e, w) = graphs.make_complete(n)
    elif tp == "gridcycle":
        (e, w) = graphs.make_gridcycle(n)
    else:
        raise Exception("unknown type")

    # Set initial labels.
    if len(init) > 0:
        initial_labels = np.array(init)
    else:
        initial_labels = np.random.randint(0, colors, size=n)

    # Add memory.
    (e, w, initial_labels) = add_memory(e, w, initial_labels, memory)

    # Run simulation.
    counts = []
    for t in range(times):
        labels = initial_labels

        count = 0
        while not np.all(labels == labels[0]):
            next_labels = np.empty(len(labels))
            for i in range(n):
                next_labels[i] = labels[np.random.choice(e[i], p=w[i])]
            for i in range(n, len(labels)):
                next_labels[i] = labels[i-n]
            labels = next_labels
            count += 1

        counts.append(count)

    print(ID, np.mean(counts), np.std(counts), flush=True)
    return [np.mean(counts), np.std(counts), counts]
