import csv
import gzip
import numpy as np
import sys

def run(measure):
    if measure != 'mean' and measure != 'median':
        print('<measure> must be "mean" or "median"')
        quit()

    tps = ['biclique', 'bintree', 'clique', 'cycle', 'torus']

    ns = set()
    data = {}
    for tp in tps:
        data[tp] = {}
        with gzip.open('data/exp2-%s.csv.gz' % tp, 'rt') as f:
            c = csv.reader(f)
            for row in c:
                [n, p, mean, std, median] = row[1:6]
                n = int(n)
                ns.add(n)
                p = float(p)
                mean = float(mean)
                median = float(median)
                std = float(std)
                if p not in data[tp]:
                    data[tp][p] = {}
                if measure == 'mean':
                    data[tp][p][n] = '{0:.0f}'.format(mean) + ' $\pm$ ' + '{0:.0f}'.format(std)
                else:
                    data[tp][p][n] = '{0:.0f}'.format(median)

    print('$n$', end='')
    for tp in tps:
        print(' &', '\\multicolumn{2}{c|}{%s}' % tp, end='')
    print(' \\\\ \\hline')

    print('$p_0$', end='')
    for tp in tps:
        print(' &', '0.9 & 1.0', end='')
    print(' \\\\ \\hline \\hline')

    for n in sorted(ns):
        print(n, end='')

        for tp in tps:
            for p in [0.9, 1.0]:
                print(' & ', end='')
                if n not in data[tp][p]:
                    print('--', end='')
                    continue
                print(data[tp][p][n], end='')
                pass

        print(' \\\\')

if __name__ == '__main__':
    measure = 'mean'
    if len(sys.argv) > 1:
        measure = sys.argv[1]
    run(measure)
