import random
import collections

# Shuffling and sorting
xs = [ (i, j) for i in range(3) for j in range(3, 0, -1) ]
random.shuffle(xs)

# Timsort, worst case O(N log N) and best case O(N)
xss = sorted(xs, key = lambda x: x[0] )
xs.sort(key = lambda x: x[0], reverse=True)

# Iterator
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

assert [ i for i in range(10) ] == [ i for i in Counter(0, 10) ]

# Errors
try:
    Counter(1, 2, 3)
except TypeError as e:
    print(e)

# Common errors
print(KeyError('a')) # Missing key in dict
print(TypeError('b')) # Incorrect type
print(ValueError('c')) # Correct type, but incorrect value
print(NotImplementedError('d')) # Not implemented
print(StopIteration('e')) # Stop iteration

# Hashing
print(hash('a'), hash('b'))

# Built-in functions
assert all(True for i in range(10))
assert any(True if i == 2 else False for i in range(10))

assert chr(56) == '8'
assert chr(97) == 'a'
assert chr(65) == 'A'

assert (2, 0) == divmod(10, 5)

a = iter([1, 2, 3, 4, 5])
assert next(a) == 1
assert next(a) == 2

# Use sentinel to stop iteration if we reach the sentinel value
b = iter(lambda: random.randint(1, 6), 6)

# Stack
class Stack:
    def __init__(self):
        self.data = []

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.pop()
        except IndexError as e:
            print('Cannot pop from an empty stack.')

    def push(self, x):
        return self.data.append(x)

    def pop(self):
        if len(self.data) == 0:
            raise IndexError
        return self.data.pop()

    def size(self):
        return len(self.data)

s = Stack()
print(next(s))

# Queue/Deque
# Takes a max-len as the second parameter
d = collections.deque([1, 2, 3], 2)
d = collections.deque([1, 2, 3])

d.append(4)
d.appendleft('A')

assert 4 == d.pop()
assert 'A' == d.popleft()

d.rotate(-1)

assert 1 == d.pop()
assert 2 == d.popleft()

assert 1 == d.count(3)

# Defaultdict
d = collections.defaultdict(list)

d[1].append('A')
d[2].append('B')

print(d[0])
print(d[1])
print(d[2])

# PriorityQueue (basically put() and get())
import queue

q = queue.PriorityQueue(11) # max size
q.put(2)
q.put(1)
q.put(3)
print(q.get(0))

# heapq (leaner, builds a heap and operates on a list)
# What we have is heappush, heappop, heapify.
# Still a list, so min() and max() works
import heapq

h = []

heapq.heappush(h, (1, 'B'))
heapq.heappush(h, (2, 2))
heapq.heappush(h, (3, 3))

print(heapq.heappop(h))

# OrderedDict
o = collections.OrderedDict([('A', 1), ('C', 2), ('B', 3)])
print(o.popitem(last = True)) # LIFO, set False for FIFO

# binary search
def binary_search(arr, target):
    i, j = 0, len(arr)
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            i = mid + 1
        elif arr[mid] > target:
            j = mid - 1
    return -1

arr = [ i for i in range(2, 10) ]
