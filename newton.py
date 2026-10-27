#This is fixed point iteration
import math

def fpi(g, x0, k, d):
    x = x0
    for i in range(k):
        x = x - g(x)/d(x)
    xc = x
    return xc

def g(x):
    return math.log(x) + x**2 - 3   # example iteration function

def d(x):
    return math.log(x) + 2*x


approx = fpi(g, 1, 25, d)
print(approx)