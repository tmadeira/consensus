import csv
import matplotlib.pyplot as plt
import numpy as np

buckets = 30

data = {}

with open('data/fig1.csv') as f:
    c = csv.reader(f)
    for row in c:
        [tp, n, p, mean] = row[:4]
        if tp not in data:
            data[tp] = []
        data[tp].append(float(mean))

x = []
for i in np.linspace(0.1, 1.0, num=buckets):
    x.append(i)
x = x[:-1]

for tp in data:
    for i in range(len(data[tp])):
        data[tp][i] = data[tp][i] / data[tp][-1]
    data[tp] = data[tp][:-1]

plt.plot(x, np.ones(buckets-1), 'k')
plt.plot(x, data['cycle'], 'r')
plt.plot(x, data['torus'], 'g')
plt.plot(x, data['clique'], 'b')
plt.plot(x, data['path'], 'c')
plt.plot(x, data['bintree'], 'm')
plt.plot(x, data['biclique'], 'y')
plt.legend(('no memory', 'cycle', 'torus', 'clique', 'path', 'bintree', 'biclique'), loc='upper right')
plt.title('n = %s' % n)
plt.show()
