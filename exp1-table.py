import csv
import gzip
import numpy as np
import sys

def run(measure):
    if measure != 'mean' and measure != 'median':
        print('<measure> must be "mean" or "median"')
        quit()

    buckets = 30
    data = {}
    stdev = {}

    with gzip.open('data/exp1.csv.gz', 'rt') as f:
        c = csv.reader(f)
        for row in c:
            [tp, n, p, mean, stde, median] = row[:6]
            if tp == 'path':
                continue
            if tp not in data:
                data[tp] = []
                stdev[tp] = []
            if measure == 'median':
                data[tp].append(float(median))
            else:
                data[tp].append(float(mean))
                stdev[tp].append(float(stde))

    print('$p_0$', end='')
    for tp in data:
        print(' &', tp, end='')
    print(' \\\\ \\hline \\hline')

    b = list(np.linspace(0.1, 1.0, num=30))

    for i in range(len(data['cycle'])):
        print('{0:.2f}'.format(b[i]), end='')
        for tp in data:
            if measure == 'median':
                print(' &', '{0:.0f}'.format(data[tp][i]), end='')
            else:
                print(' &', '{0:.0f}'.format(data[tp][i]), '$\pm$', '{0:.0f}'.format(stdev[tp][i]), end='')
        print(' \\\\')

if __name__ == '__main__':
    measure = 'mean'
    if len(sys.argv) > 1:
        measure = sys.argv[1]
    run(measure)
