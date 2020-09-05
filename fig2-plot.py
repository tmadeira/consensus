import csv
import gzip
import matplotlib.pyplot as plt
import numpy as np

for tp in ['clique', 'torus', 'cycle', 'path']:
    for measure in ['mean', 'median']:
        data = {}
        x = []

        with gzip.open('fig2-%s.csv.gz' % tp, 'rt') as f:
            c = csv.reader(f)
            for row in c:
                [n, p, mean, _, median] = row[1:6]
                n = int(n)
                p = float(p)
                mean = float(mean)
                median = float(median)
                if p not in data:
                    data[p] = []
                if p == 1:
                    x.append(n)
                if measure == 'mean':
                    data[p].append(mean)
                else:
                    data[p].append(median)

        for p in data:
            if p == 1:
                continue
            for i in range(len(data[p])):
                data[p][i] = data[p][i] / data[1][i]

        for i in range(len(data[1])):
            data[1][i] = 1

        plt.plot(x, data[1.0], 'k')
        plt.plot(x, data[0.9], 'b')
        plt.plot(x, data[0.8], 'r')
        plt.legend(('p=1', 'p=0.9', 'p=0.8'), loc='upper right')
        plt.title('%s (%s)' % (tp, measure))
        plt.show()
