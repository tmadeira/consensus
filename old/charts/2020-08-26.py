import csv
import matplotlib.pyplot as plt
import numpy as np

data = {}

with open('../src/2020-08-26.txt') as f:
    c = csv.reader(f, delimiter=' ')
    for row in c:
        [tp, n, p, mean] = row[:4]
        if n not in data:
            data[n] = {}
        if tp not in data[n]:
            data[n][tp] = []
        data[n][tp].append(float(mean))

x = []
for i in np.linspace(0.1, 1.0, num=50):
    x.append(i)

for n in data:
    for tp in data[n]:
        for i in range(len(data[n][tp])):
            data[n][tp][i] = data[n][tp][i] / data[n][tp][-1]
    plt.plot(x, np.ones(50), 'k')
    plt.plot(x, data[n]['cycle'], 'r')
    plt.plot(x, data[n]['complete'], 'g')
    plt.plot(x, data[n]['gridcycle'], 'b')
    plt.plot(x, data[n]['expandedcycle'], 'y')
    plt.legend(('no memory', 'cycle', 'complete', 'grid cycle', 'expanded cycle'), loc='upper right')
    plt.title('n = %s' % n)
    plt.show()

"""
name = ['alternate cycle (0101...1010)', 'worst-case cycle (0...01...1)', 'complete graph']

for start in [0, 1, 2]:
    x = []
    plots = [[], [], []]
    for d in data:
        if d[0] == start:
            x.append(d[1])
        if d[0] % 3 != start:
            continue
        plots[d[0] // 3].append(d[2])

    plt.plot(x, plots[0], 'r', x, plots[1], 'b', x, plots[2], 'g')
    plt.legend(('n=17', 'n=31', 'n=43'), loc='lower left')
    plt.title(name[start])
    plt.show()
"""
