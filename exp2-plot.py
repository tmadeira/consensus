import csv
import gzip
import matplotlib.pyplot as plt
import numpy as np
import sys

def run(measure):
    if measure != 'mean' and measure != 'median':
        print('<measure> must be "mean" or "median"')
        quit()
    colors = 'rgbcmy'
    col = 0

    tps = ['biclique', 'bintree', 'clique', 'cycle', 'torus']

    plt.plot(list(range(0, 2050)), [1] * 2050, 'k')

    for tp in tps:
        with gzip.open('data/exp2-%s.csv.gz' % tp, 'rt') as f:
            c = csv.reader(f)
            x = []
            y = []
            for row in c:
                [n, p, mean, _, median] = row[1:6]
                n = int(n)
                p = float(p)
                val = float(mean)
                if measure == 'median':
                    val = float(median)
                if p == 0.9:
                    x.append(n)
                    y.append(val)
                elif p == 1:
                    y[len(y)-1] /= val

            plt.plot(x, y, colors[col])
            col += 1

    plt.legend(['baseline'] + tps, loc='upper right')
    plt.title('exp. 2 (p=0.9, times=10000)')
    plt.show()

if __name__ == '__main__':
    measure = 'mean'
    if len(sys.argv) > 1:
        measure = sys.argv[1]
    run(measure)
