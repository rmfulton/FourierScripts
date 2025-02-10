import numpy as np 
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.style.use('dark_background')
"""
Dirichlet's Test for convergence uses the summation by Parts formula
Sum_{n=M}^{N} a_nb_n  = a_NB_N - a_MB_{M-1} - SUM_{n=M}^{N-1} (a_{n+1}  - a_n)B_n
to show that 
1. If a_n is a sequence of reals decreasing monotonically to 0, and 
2. B_N is the Nth partial sum of the terms b_i, 
3. B_N are all bounded by B, then

| Sum_{n=M}^{\infty} a_nb_n | < 2a_nB
This provides an upper bound on the distance between 
the nth zipper sum and the zipper series
"""

def DirichletBound(n, a_n, B):
    return 2*a_n*B

def ex7_a_n(n):
    return 1/np.log(n)
def ex7_B_n(n,x):
    return np.sin(n*x)
"""
the sum of sin(nx) from 2 up to infinity is never more than 
1/sin(x/2)
"""
def ex7_B(x):
    return 1/np.sin(x/2)

def nthPartialSum_ex7(n):
    def partialSum(x):
        S = 0
        for i in range(2,n+1):
            S += ex7_B_n(i,x)/ex7_a_n(i)
        return S
    return partialSum

def nthDirichletBound_ex7(n):
    def bound(x):
        return DirichletBound(n, ex7_a_n(n), ex7_B(abs(x)))
    return bound

def PlotNthPartialSumAndEnvelope(terms, step):
    x = np.arange(-0.1, 0.1,step)
    f = nthPartialSum_ex7(terms)
    e = nthDirichletBound_ex7(terms)
    y = [f(el) for el in x]
    envelope = [e(el) for el in x]
    above = [y[i] + envelope[i] for i in range(len(x))]
    below = [y[i] - envelope[i] for i in range(len(x))]
    # ax.plot(x,y,color='b')
    ax.plot(x,above, color='g')
    ax.plot(x,below, color='r')
    ax.fill_between(x, above, below, color='b')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')


PlotNthPartialSumAndEnvelope(terms=1600, step = 0.0005)
plt.show()



