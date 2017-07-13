from random import shuffle
from time import time

N = 10000

A = [ i for i in range(N) ]
B = list(A)
shuffle(B)

def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i += 1
        else:
            S[j + i] = S2[j]
            j += 1

    return S

def merge_sort(S):
    n = len(S)
    if n < 2:
        return S

    mid = n // 2
    S1 = merge_sort(S[0:mid])
    S2 = merge_sort(S[mid:n])

    return merge(S1, S2, S)


start = time()
C = merge_sort(B)
end = time()
print(end - start)

assert A == C
