import csv
import gzip
import numpy as np
import sys

def run(measure):
    if measure != 'mean' and measure != 'median':
        print('<measure> must be "mean" or "median"')
        quit()
    tps = ['biclique', 'bintree', 'clique', 'cycle', 'torus']

    legend = []
    for tp in tps:
        with gzip.open('data/exp2-%s.csv.gz' % tp, 'rt') as f:
            c = csv.reader(f)
            x = []
            y = []
            for row in c:
                [n, p, mean, _, median] = row[1:6]
                n = int(n)
                p = float(p)
                mean = float(mean)
                median = float(median)

                if measure == 'mean':
                    val = mean
                else:
                    val = median

                if p == 0.9:
                    x.append(n)
                    y.append(val)
                elif p == 1:
                    y[len(y)-1] /= val

            print("\\addplot coordinates {")
            for i in range(len(y)):
                print("\t(%f, %f)" % (x[i], y[i]))
            print("};")

            legend.append(tp)

    print("\\legend{" + ",".join(legend) + "}")

if __name__ == '__main__':
    measure = 'mean'
    if len(sys.argv) > 1:
        measure = sys.argv[1]
    run(measure)
