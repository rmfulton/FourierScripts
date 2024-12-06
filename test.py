import random
import math

for _ in range(20):
    x = random.random()
    print(f"random is {x}")
    pi = math.pi
    numer = 0
    denom = 0
    for n in range(1,1_000_000_000):
        numer += abs(math.sin(n*2*pi*x))/n
        denom += 1/n
    print(f"result was    {numer/denom}")
    print(f"versus 2/pi = {2/pi}")
    print("")
