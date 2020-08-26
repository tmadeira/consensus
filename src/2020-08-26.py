"""
Experiment: Given 4 structures, test memory distribution to generate a chart
for the paper.

Setup:
- n = 81, times = 1000
- 4 graphs (cycle, complete graph, gridcycle, expanded cycle)
- uniform random initial vectors
- 50 tests for each graph, with memory uniformly ranging from [0.01, 0.99] to [1.00, 0.00]
"""

from multiprocessing import Pool
import numpy as np

import simulation

P = 6
n = 81
buckets = 50
times = 1000

tps = [
    'cycle',
    'complete',
    'gridcycle',
    #'expandedcycle',
]

# Create tasks.
tasks = []
seed = 0
for p in np.linspace(0.1, 1.00, num=buckets):
    for tp in tps:
        tasks.append({
          'seed': seed,
          'mem': [p, 1-p],
          'n': n,
          'tp': tp,
        })
        seed += 1

def run_task(task):
    return simulation.run(task['n'],
        seed=task['seed'],
        tp=task['tp'],
        memory=task['mem'],
        ID='%s %f' % (task['tp'], task['mem'][0]),
        times=times,
    )

p = Pool(P)
results = p.map(run_task, tasks)

for i in range(len(tasks)):
  print(tasks[i]['tp'], tasks[i]['mem'][0], results[i][0], results[i][1], results[i][2])
