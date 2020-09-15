import csv
import gzip
import numpy as np

def run():
    buckets = 30
    data = {}

    with gzip.open('data/exp1.csv.gz', 'rt') as f:
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

    legend = []
    for tp in data:
        for i in range(len(data[tp])):
            data[tp][i] = data[tp][i] / data[tp][-1]
        data[tp] = data[tp][:-1]

        print("\\addplot coordinates {")
        for i in range(len(data[tp])):
            print("\t(%f, %f)" % (x[i], data[tp][i]))
        print("};")

        legend.append(tp)

    print("\\legend{" + ",".join(legend) + "}")

if __name__ == '__main__':
    run()
