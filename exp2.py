import csv
import multiprocessing
import numpy as np
import os
import time

def run_experiment(tp, n, writer):
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

def run():
    times = 10000
    threads = multiprocessing.cpu_count()

    # Powers of two (9) - n in range [7, 2047].
    for tp in ['bintree']:
        with open('data/exp2-%s.csv' % tp, 'w') as f:
            writer = csv.writer(f)
            for m in range(3, 12):
                n = 2**m-1
                run_experiment(tp, n, writer)

    # Odd perfect squares - n in range [9, 2025].
    for tp in ['biclique', 'clique', 'cycle', 'torus']:
        with open('data/exp2-%s.csv' % tp, 'w') as f:
            writer = csv.writer(f)
            for m in range(3, 46, 2):
                n = m*m
                run_experiment(tp, n, writer)

if __name__ == '__main__':
    run()
