"""
Experiment: Test different memory distributions.

Setup:
- 3 graphs (alternate cycle, worst cycle and random complete graph)
- 20 tests for each graph, with memory uniformly ranging from [0.01, 0.99] to [0.99, 0.01]
"""

N = 201

from multiprocessing import Pool
import numpy as np

import simulation

# Build init vectors.
alternate = []
worst = []
for i in range(N):
  alternate.append(i % 2)
  worst.append(2 * i // N)

# Setup tests.
setup = [
  {
    'init': alternate,
    'tp': 'cycle',
  },
  {
    'init': worst,
    'tp': 'cycle',
  },
  {
    'init': alternate,
    'tp': 'complete',
  },
]

# Create tasks.
tasks = []
for i in np.linspace(0.1, 0.99, num=20):
  for j in range(len(setup)):
    tasks.append({
      'mem': [i, 1-i],
      'setup': j,
      'init': setup[j]['init'],
      'tp': setup[j]['tp'],
    })

def run_task(task):
  return simulation.run(len(task['init']),
    init=task['init'],
    tp=task['tp'],
    memory=task['mem'],
    times=200,
  )

p = Pool(6)
results = p.map(run_task, tasks)

for i in range(len(tasks)):
  print(results[i][0], results[i][1], tasks[i]['mem'][0], tasks[i]['setup'])
