import csv
import multiprocessing
import numpy as np
import os
import time

n = 441
times = 1000

threads = multiprocessing.cpu_count()

start = time.time()

with open('fig1.csv', 'w') as f:
    writer = csv.writer(f)
    for tp in ['clique', 'torus', 'cycle']:
        for p in np.linspace(0.1, 1.0, num=30):
            stream = os.popen('./simulator %s %d %d %f %d' % (tp, n, times, p, threads))
            results = list(map(int, stream.read().strip().split('\n')))
            print(time.time() - start, 'seconds elapsed.')
            print('finished', tp, n)
            print('avg:', np.mean(results))
            print('stdev:', np.std(results))
            print('median:', np.median(results))
            print('')
            writer.writerow([tp, n, p, np.mean(results), np.std(results), np.mean(results)] + results)
