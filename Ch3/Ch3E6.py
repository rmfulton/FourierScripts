import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')
"""
This is to plot the trigonometric 
polynomials whose fourier coefficients are 1/k
for -n <= k <= n
"""
def partialSum(N):
    def poly(x):         
        S = 0
        for i in range(1,N+1):
            S += np.sin(i*x)
        return S
    return poly


def plotPartialSum(N):
    f = partialSum(N)
    x = np.arange(-np.pi, np.pi, 0.001)
    y = [f(el) for el in x]
    plt.plot(x, y)
    # plt.grid()

for i in range(1,7):
    plotPartialSum(i)
# plotPartialSum(100)
plt.show()