"""
Experiment: Test all combinations (orders) for initial vector.

Result: 0...01...1 is the worst case (in particular, worse than 0101...1010).
"""

import numpy as np
import simulation

n = 9
sn = 2**n

for S in range(sn):
    init = np.zeros(n)
    for i in range(n):
        if (2**i) & S:
            init[i] = 1
    print(simulation.run(n, memory=[0.8, 0.2], init=init))
