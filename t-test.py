import math

# https://lse-methodology.github.io/MY464/c-means.html#c-means
def calc_t(n, y1, s1, y2, s2):
    n1 = n2 = n

    # Eq. 11
    num = (n2 - 1) * (s2 ** 2) + (n1 - 1) * (s1 ** 2)
    den = n1 + n2 - 2
    sig = math.sqrt(num / den)

    # Eq. 12
    num = y2 - y1
    den = sig * math.sqrt(1/n2 + 1/n1)
    t = num / den

    return t

t = calc_t(10000, 3258.6267, 2355.2667652618693, 3922.6187, 2888.5997517327164)
print("Exp. 2 | torus, n = 1089 | t =", t)

t = calc_t(10000, 8944.5506, 7163.029972507419, 14970.3761, 11751.004531572982)
print("Exp. 2 | bintree, n = 1023 | t =", t)

t = calc_t(10000, 1852.127, 1367.0338225775542, 155156.7083, 266236.29921102425)
print("Exp. 2 | biclique, n = 1089 | t =", t)

t = calc_t(10000, 1844.3936, 1340.9593774902503, 1521.7053, 1110.572404146578)
print("Exp. 2 | clique, n = 1089 | t =", t)

t = calc_t(10000, 135232.4427, 131922.37933843266, 482572.0532, 477517.8876667864)
print("Exp. 2 | cycle, n = 1089 | t =", t)
