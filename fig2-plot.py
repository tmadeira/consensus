import csv
import gzip
import matplotlib.pyplot as plt
import numpy as np

colors = 'rgbcmy'
col = 0

tps = ['biclique', 'bintree', 'clique', 'cycle', 'torus', 'path']

plt.plot(list(range(0, 1600)), [1] * 1600, 'k')

for tp in tps:
    with gzip.open('data/fig2-%s.csv.gz' % tp, 'rt') as f:
        c = csv.reader(f)
        x = []
        y = []
        for row in c:
            [n, p, mean] = row[1:4]
            n = int(n)
            p = float(p)
            mean = float(mean)
            if p == 0.9:
                x.append(n)
                y.append(mean)
            elif p == 1:
                y[len(y)-1] /= mean

        plt.plot(x, y, colors[col])
        col += 1

plt.legend(['baseline'] + tps, loc='upper right')
plt.title('fig. 2 (p=0.9, times=10000)')
plt.show()

