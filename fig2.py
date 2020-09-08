import csv
import multiprocessing
import numpy as np
import os
import time

times = 10000
threads = multiprocessing.cpu_count()

def run(tp, n, writer):
    start = time.time()
    for p in [0.9, 1]:
        stream = os.popen('./simulator %s %d %d %f %d' % (tp, n, times, p, threads))
        results = list(map(int, stream.read().strip().split('\n')))
        print(time.time() - start, 'seconds elapsed.')
        print('finished', tp, n, p)
        print('avg:', np.mean(results))
        print('stdev:', np.std(results))
        print('median:', np.median(results))
        print('')
        writer.writerow([tp, n, p, np.mean(results), np.std(results), np.median(results)] + results)

# Powers of two (9) - n in range [7, 2047].
for tp in ['bintree']:
    with open('fig2-%s.csv' % tp, 'w') as f:
        writer = csv.writer(f)
        for m in range(3, 12):
            n = 2**m-1
            run(tp, n, writer)

# Odd perfect squares - n in range [9, 2025].
for tp in ['biclique', 'clique', 'cycle', 'path', 'torus']:
    with open('fig2-%s.csv' % tp, 'w') as f:
        writer = csv.writer(f)
        for m in range(3, 46, 2):
            n = m*m
            run(tp, n, writer)
