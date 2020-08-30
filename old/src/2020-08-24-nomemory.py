"""
Experiment: Find time distribution for fixed parameters.

Setup:
- n_1 = 17, n_2 = 25, times = 2000, mem = [0.8, 0.2]
- 3 graphs (alternate cycle, worst cycle and random complete graph)
"""

from multiprocessing import Pool
import numpy as np

import simulation

P = 6
N = [17, 25]
setup = []

for n in N:
    # Build init vectors.
    alternate = []
    worst = []
    for i in range(n):
      alternate.append(i % 2)
      worst.append(2 * i // n)

    setup.append({'n': n, 'init': alternate, 'tp': 'cycle'})
    setup.append({'n': n, 'init': worst, 'tp': 'cycle'})
    setup.append({'n': n, 'init': alternate, 'tp': 'complete'})

# Create tasks.
tasks = []
for j in range(len(setup)):
    tasks.append({
        'mem': [1.0],
        'setup': j,
        'n': setup[j]['n'],
        'init': setup[j]['init'],
        'tp': setup[j]['tp'],
    })

def run_task(task):
    return simulation.run(len(task['init']),
        init=task['init'],
        tp=task['tp'],
        memory=task['mem'],
        ID='%d %f' % (task['setup'], task['mem'][0]),
        times=2000,
    )

p = Pool(P)
results = p.map(run_task, tasks)

import csv
import sys

w = csv.writer(sys.stdout)
for i in range(len(tasks)):
    row = [tasks[i]['setup']] + results[i][2]
    w.writerow(row)
