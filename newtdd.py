import numpy as np


def newtdd(x,y):
    n = len(x)
    v = np.zeros((n,n))
    for j in range(n):
        v[j, 0] = y[j]
    for i in range(1, n):
        for j in range(n - i):
            v[j, i] = (v[j + 1, i - 1] - v[j, i - 1]) / (x[j + i] - x[j])

    c = v[0, :n]
    return c