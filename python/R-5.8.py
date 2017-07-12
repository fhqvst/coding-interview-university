from time import time
from functools import reduce
n = 100000
tests = 1000
timing = []
for t in range(tests):
	data = [ None for k in range(n) ]
	time1 = time()
	data.pop(n // 2)
	time2 = time()
	timing.append(time2 - time1)

avg = reduce(lambda x, y: x + y, timing) / len(timing)
print(avg)
