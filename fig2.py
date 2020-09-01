import csv
import multiprocessing
import numpy as np
import os
import time

times = 100000

threads = multiprocessing.cpu_count()

for tp in ['cycle', 'clique', 'torus']:
    start = time.time()

    with open('fig2-%s.csv' % tp, 'w') as f:
        writer = csv.writer(f)
        for m in range(3, 52, 2):
            n = m*m
            for p in [0.8, 0.9, 1]:
                stream = os.popen('./simulator %s %d %d %f %d' % (tp, n, times, p, threads))
                results = list(map(int, stream.read().strip().split('\n')))
                print(time.time() - start, 'seconds elapsed.')
                print('finished', tp, n, p)
                print('avg:', np.mean(results))
                print('stdev:', np.std(results))
                print('median:', np.median(results))
                print('')
                writer.writerow([tp, n, p, np.mean(results), np.std(results), np.mean(results)] + results)
