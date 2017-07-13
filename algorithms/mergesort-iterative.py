"""
This implementation performs a bottom-up merge sort.
First we sort all pairs (length 2), then do the same but for length 4, and so on.

It is slightly faster than regular mergesort since it avoids the overhead from
recursive calls and temporary memory.
"""
import math
from random import shuffle
from time import time

N = 10000

A = [ i for i in range(N) ]
B = list(A)
shuffle(B)

def merge(S, D, start, inc):
    end1 = start + inc
    end2 = min(start + (2 * inc), len(S))

    x = start
    y = start + inc
    z = start

    while x < end1 and y < end2:
        if S[x] < S[y]:
            D[z] = S[x]
            x += 1
        else:
            D[z] = S[y]
            y += 1
        z += 1

    if x < end1:
        D[z:end2] = S[x:end1]

    if y < end2:
        D[z:end2] = S[y:end2]

def merge_sort(S):
    n = len(S)
    logn = math.ceil(math.log(n, 2))

    src = S
    dest = [None] * n

    for i in (2**k for k in range(logn)):
        for j in range(0, n, 2*i):
            merge(src, dest, j, i)
        src, dest = dest, src
    if S is not src:
        S[0:n] = src[0:n]

    return S

start = time()
C = merge_sort(B)
end = time()
print(end - start)

assert A == C
