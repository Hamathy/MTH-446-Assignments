import numpy as np
import matplotlib.pyplot as plt


def clickinterp():
    xl, xr = -3, 3
    yb, yt = -3, 3

    xlist = []
    ylist = []

    fig, ax = plt.subplots()
    ax.axhline(0, color='k')
    ax.axvline(0, color='k')
    ax.grid(True)
    ax.set_xlim(xl, xr)
    ax.set_ylim(yb, yt)

    while True:
        pts = plt.ginput(1, timeout=-1)

        if len(pts) == 0:
            break

        xnew, ynew = pts[0]

        xlist.append(xnew)
        ylist.append(ynew)

        k = len(xlist)

        c = newtdd(np.array(xlist), np.array(ylist), k)

        x = np.arange(xl, xr + 0.01, 0.01)
        y = nest(k - 1, c, x, np.array(xlist))

        ax.clear()
        ax.plot(xlist, ylist, 'o')
        ax.plot(x, y)

        ax.axhline(0, color='k')
        ax.axvline(0, color='k')

        ax.set_xlim(xl, xr)
        ax.set_ylim(yb, yt)
        ax.grid(True)

        plt.draw()

    plt.show()

def newtdd(x, y, n):
    # Initialize Newton triangle
    v = np.zeros((n, n))

    # Fill first column with y values
    for j in range(n):
        v[j, 0] = y[j]

    # Compute divided differences
    for i in range(1, n):          # corresponds to MATLAB i=2:n
        for j in range(n - i):
            v[j, i] = (v[j + 1, i - 1] - v[j, i - 1]) / (x[j + i] - x[j])

    # Read coefficients from top row
    c = np.zeros(n)
    for i in range(n):
        c[i] = v[0, i]

    return c


def nest(d, c, x, b=None):
    # If no base points are provided, use zeros
    if b is None:
        b = np.zeros(d)

    # Start with highest-degree coefficient
    y = c[d]

    # Nested multiplication
    for i in range(d - 1, -1, -1):
        y = y * (x - b[i]) + c[i]

    return y


x = [0, 1, 2, 3]
y = [3, 6, 11, -9]
c = newtdd(x, y, len(x))
xx = np.arange(0, 4.01, 0.01)
yy = nest(2, c, xx, x)
#plt.plot(x, y, 'o', label='Data Points')
#plt.plot(xx, yy, label='Interpolation')
#plt.legend()
#plt.grid(True)
#plt.show()
clickinterp()