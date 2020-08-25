import csv
import matplotlib.pyplot as plt

name = [
    'alternate cycle, n=17, NO MEMORY',
    'worst cycle, n=17, NO MEMORY',
    'complete graph, n=17, NO MEMORY',
    'alternate cycle, n=25, NO MEMORY',
    'worst cycle, n=25, NO MEMORY',
    'complete graph, n=25, NO MEMORY',
]

with open('../src/2020-08-24-nomemory.csv') as f:
    c = csv.reader(f)
    for row in c:
        for i in range(len(row)):
            row[i] = int(row[i])
        plt.hist(row[1:], 50)
        plt.title(name[int(row[0])])
        plt.show()
