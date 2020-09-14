import csv
import numpy as np
import gzip

def run():
    tps = ['biclique', 'bintree', 'clique', 'cycle', 'torus']

    legend = []
    for tp in tps:
        with gzip.open('data/exp2-%s.csv.gz' % tp, 'rt') as f:
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

            print("\\addplot coordinates {")
            for i in range(len(y)):
                print("\t(%f, %f)" % (x[i], y[i]))
            print("};")

            legend.append(tp)

    print("\\legend{" + ",".join(legend) + "}")

if __name__ == '__main__':
    run()
