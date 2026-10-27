import numpy as np
from newtdd import newtdd
from nest import nest

x0 = np.array([1.,2.,3.,4.,5.,6.,7.,8.])
y0 = np.array([2.,3.,4.,5.,6.,7.,8.,10.])

c = newtdd(x0, y0)
value = nest(c, 9, x0)

print("P(9) =", value)