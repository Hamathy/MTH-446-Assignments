import numpy as np

def bisection_method():
    f = lambda x: 24*np.exp(5*x**3)-(625*x**12 - 1000*x**9 + 750*x**6 - 240*x**3 + 33)*np.exp(3)
    a = 0.
    b = 1.
    for i in range(30):
        c = (a+b)/2
        print(c)
        if f(c) == 0:
            break
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
    xc = (a+b)/2
    print(xc)
bisection_method()