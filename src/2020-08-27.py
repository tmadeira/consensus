"""
TODO: Describe experiment.
"""

from multiprocessing import Pool
import csv
import numpy as np
import random
import sys

import simulation

workers = [
    {'name': 'madeira-desktop', 'cores': 6},
    {'name': 'madeira-mac', 'cores': 4},
    {'name': 'gauy-desktop', 'cores': 8},
    {'name': 'david-mac', 'cores': 8},
]

# remaining parameters
N = [441]
buckets = 40
times = 200
tps = [
    'path',
    'cycle',
    'gridcycle',
    'complete',
]

def run_task(task):
    return simulation.run(task['n'],
        tp=task['tp'],
        memory=task['mem'],
        ID='%s %f' % (task['tp'], task['mem'][0]),
        times=times,
        rand_init=True,
    )

def run(worker):
    # Create tasks.
    tasks = []
    for n in N:
        for p in np.linspace(0.1, 1.00, num=buckets):
            for tp in tps:
                tasks.append({
                  'mem': [p, 1-p],
                  'n': n,
                  'tp': tp,
                })

    random.seed(0)
    random.shuffle(tasks)

    total_tasks = len(tasks)

    start = -1
    end = -1
    cores = -1

    total_cores = 0
    for w in workers:
        if worker == w['name']:
            start = total_cores
            cores = w['cores']
            end = total_cores + cores

        total_cores += w['cores']

    if start == -1:
        print('Invalid worker.')
        quit()

    start *= total_tasks / total_cores
    end *= total_tasks / total_cores
    start = int(start)
    end = int(end)

    print('Running tasks for %s (%d-%d)...' % (worker, start, end))

    with open('2020-08-27-%s.csv' % worker, 'w') as f:
        writer = csv.writer(f)

        p = Pool(cores)
        results = p.map(run_task, tasks[start:end])

        for i in range(start, end):
            writer.writerow([
                    tasks[i]['tp'],
                    tasks[i]['n'],
                    tasks[i]['mem'][0],
                    results[i-start][0],
                    results[i-start][1],
                    results[i-start][2]
                ] + results[i-start][3])

if __name__ == '__main__':
    names = list(map(lambda x: x['name'], workers))

    if len(sys.argv) < 2 or sys.argv[1] not in names:
        print('Usage: %s <worker>' % sys.argv[0])
        print('<worker> must be one of', names)
        quit()

    run(sys.argv[1])
