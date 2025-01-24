import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

def plotFejer(N):
    x = np.arange(-np.pi, np.pi, 0.001)
    y = np.sin(N*x/2)**2/np.sin(x/2)**2/N
    plt.plot(x, y)
    plt.show()


def plotFejerUpTo(N):
    x = np.arange(-np.pi, np.pi, 0.001)
    for i in range(1, N):
        y = np.sin(i*x/2)**2/np.sin(x/2)**2/i
        plt.plot(x, y)
    plt.show()

plotFejerUpTo(15)