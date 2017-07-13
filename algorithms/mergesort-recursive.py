"""
Take caution.
This version is about 4000% slower than the one in mergesort.py, mostly due to
the heavy use of the call stack. It is a PoC more than anything else.
"""

from random import shuffle
from time import time
from sys import setrecursionlimit

N = 10000

setrecursionlimit(N + 3)

A = [ i for i in range(N) ]
B = list(A)
shuffle(B)

def merge(S1, S2):
    if (S1 == []): return S2
    if (S2 == []): return S1

    X, *XS = S1
    Y, *YS = S2
    return [X] + merge(XS, S2) if X < Y else [Y] + merge(S1, YS)

def merge_sort(S):
    n = len(S)
    if (n < 2): return S

    XS = merge_sort(S[0 : n // 2])
    YS = merge_sort(S[n // 2 : ])

    return merge(XS, YS)

start = time()
C = merge_sort(B)
end = time()
print(end - start)

assert A == C
