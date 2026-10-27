import numpy as np
def nest(c,x,b=None):
    d = len(c)-1
    if b is None:
        b=np.zeros(d)
    y = c[d]
    for i in range(d-1,-1,-1):
        y = y*(x-b[i])+c[i]
    return y