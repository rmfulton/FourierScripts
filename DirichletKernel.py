import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

def plotDirichlet(N):
    x = np.arange(-np.pi, np.pi, 0.001)
    y = np.sin((N+0.5)*x)/np.sin(x/2)
    plt.plot(x, y)
    plt.show()


def plotDirichletUpTo(N):
    x = np.arange(-np.pi, np.pi, 0.001)
    for i in range(1, N):
        y = np.sin((i+0.5)*x)/np.sin(x/2)
        plt.plot(x, y)
    plt.show()

plotDirichletUpTo(7)