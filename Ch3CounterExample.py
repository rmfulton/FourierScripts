import numpy as np
import matplotlib.pyplot as plt
import cmath
plt.style.use('dark_background')

thickness = 1
"""

"""
def SawTooth(x):
    theta = x % 2*np.pi
    return complex(0,1)*(np.pi-theta)

def FourierSumSawToothN(N):
    def partialSum(x):
        theta = x % 2*np.pi
        S = complex(0,0)
        for i in range(1,N+1):
            S += 2*complex(0,1)*np.sin(i*theta)/i
        return S
    return partialSum

def FourierSumSawToothTildaN(N):
    def partialSumTilda(x):
        theta = x % 2*np.pi
        S = complex(0,0)
        for i in range(-1,-N-1,-1):
            S += (np.cos(i*theta) + complex(0,1)*np.sin(i*theta))/i
        return S
    return partialSumTilda

def plotSawTooth():
    x = np.arange(-np.pi, np.pi, 0.01)
    y = [SawTooth(el).imag for el in x]
    # z = [SawTooth(el).real for el in x]
    plt.scatter(x,y, s=thickness)
    # plt.scatter(x,z)

def plotPartialSum(N):
    x = np.arange(-np.pi, np.pi, 0.01)
    partialSum = FourierSumSawToothN(N)
    y = [partialSum(el).imag for el in x]
    # z = [partialSum(el).real for el in x]
    plt.scatter(x,y,s=thickness)
    # plt.scatter(x,z)
def PlotFourierSumSawToothTildaN(N):
    x = np.arange(-np.pi, np.pi, 0.001)
    partialSum = FourierSumSawToothTildaN(N)
    y = [abs(partialSum(el)) for el in x]
    # z = [partialSum(el).real for el in x]
    plt.scatter(x,y,s=thickness)
    # plt.scatter(x,z, s=thickness)

k = 400
plotSawTooth()
# plotPartialSum(k)
PlotFourierSumSawToothTildaN(k)
plt.show()