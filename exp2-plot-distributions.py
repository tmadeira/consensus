import csv
import gzip
import matplotlib.pyplot as plt
import numpy as np
import sys

def run():
    bins = 100
    tps = ['biclique', 'bintree', 'clique', 'cycle', 'torus']

    for tp in tps:
        p09 = []
        p10 = []

        with gzip.open('data/exp2-%s.csv.gz' % tp, 'rt') as f:
            c = csv.reader(f)
            for row in c:
                [n, p] = row[1:3]
                n = int(n)

                if n != 2025 and n != 2047:
                    continue

                p = float(p)
                results = list(map(float, row[6:]))

                if p == 0.9:
                    p09 = results
                elif p == 1:
                    p10 = results

        f = plt.figure()
        plt.hist([p09, p10], bins=bins, histtype='bar')
        plt.legend(['0.9', '1.0'])
        f.savefig('plots/dist-%s.pdf' % tp, bbox_inches='tight')

if __name__ == '__main__':
    run()
