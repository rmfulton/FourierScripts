import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

def plotPoisson(N):
    r = 1 - 1/N
    x = np.arange(-np.pi, np.pi, 0.001)
    y = (1-r**2)/(1-2*r*np.cos(x) + r**2)
    plt.plot(x, y)
    plt.show()


def plotPoissonUpTo(N):
    x = np.arange(-np.pi, np.pi, 0.001)
    for i in range(1, N):
        r = i/N
        y = (1-r**2)/(1-2*r*np.cos(x) + r**2)
        plt.plot(x, y)
    plt.show()

plotPoissonUpTo(100)