import csv
import matplotlib.pyplot as plt

name = [
    'alternate cycle, n=17',
    'worst cycle, n=17',
    'complete graph, n=17',
    'alternate cycle, n=25',
    'worst cycle, n=25',
    'complete graph, n=25',
]

with open('../src/2020-08-24.csv') as f:
    c = csv.reader(f)
    for row in c:
        for i in range(len(row)):
            row[i] = int(row[i])
        plt.hist(row[1:], 50)
        plt.title(name[int(row[0])])
        plt.show()
