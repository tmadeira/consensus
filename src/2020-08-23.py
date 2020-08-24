"""
Experiment: Redo last experiment but for smaller N, testing no memory and
increasing times from 200 to 1000 in order to seek smoother graphs.

Setup:
- n_1 = 17, n_2 = 31, n_3 = 43, times = 1000
- 3 graphs (alternate cycle, worst cycle and random complete graph)
- 40 tests for each graph, with memory uniformly ranging from [0.01, 0.99] to [1.00, 0.00]
"""

from multiprocessing import Pool
import numpy as np

import simulation

P = 12
N = [17, 31, 43]
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
for i in np.linspace(0.1, 1.00, num=40):
  for j in range(len(setup)):
    tasks.append({
      'mem': [i, 1-i],
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
    times=1000,
  )

p = Pool(P)
results = p.map(run_task, tasks)

for i in range(len(tasks)):
  print(tasks[i]['setup'], tasks[i]['mem'][0], results[i][0], results[i][1])
