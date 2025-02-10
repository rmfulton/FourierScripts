import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('dark_background')

def HeatKernel(N,t):
    def Ht(x):
        s = 1
        for i in range(1, N+1):
            theta = 2*np.pi*x
            s += 2*np.exp(-4*np.pi**2 * i**2 * t) * np.cos(theta)
        return s
    return Ht



def plotHeat(N,t):
    x = np.arange(0, 1, 0.001)
    Ht = HeatKernel(N,t)
    y = [Ht(el) for el in x]
    plt.plot(x, y)


def plotHeatUpTo(N):
    x = np.arange(-np.pi, np.pi, 0.001)
    M = 100
    for i in range(1, N+1):
        t = 1/N
        plotHeat(M,t)
    plt.show()

plotHeat(N=100,t=1/1000)
plt.show()