import numpy as np
import matplotlib.pyplot as plt
from newtdd import newtdd
from nest import nest
n = 6
f = lambda x: np.exp(-5.*x*x)
x0 = np.linspace(-2.,2.,n)
y0 = f(x0)
x = np.linspace(-2.,2.,200)
y = f(x)
yinterp = nest(newtdd(x0,y0),x,x0)
fig,axs = plt.subplots(2)
axs[0].plot(x0,y0,'ro',x,yinterp,'g',x,y,'b')
axs[0].grid()
fig.show()

