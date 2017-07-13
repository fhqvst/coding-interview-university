from timeit import default_timer as timer
from random import random
import math
import matplotlib.pyplot as plt

# Sort an array of given size, and return average time
def run_test(size):
    tests = 1000
    runs = []
    for i in range(tests):
        arr = [ random() for x in range(size) ]
        start = timer()
        arr.sort()
        end = timer()
        runs.append(end - start)
    
    average = 0
    for i in range(tests):
        average += (runs[i] / tests)
    return average

# Build x's and y's to plot
x = [ 10 * i for i in range(1, 51) ]
y_test = [ run_test(size) for size in x ]

# Scale the actual n * log (n) with the hidden coefficient
c = .000000023
y_actual = [ c * size * math.log(size) for size in x ]

# Plot it
plt.plot(x, y_test, 'ro')
plt.plot(x, y_actual, 'bo')
plt.yscale('log')
plt.show()
