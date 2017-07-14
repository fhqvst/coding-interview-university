from random import shuffle
from time import time

N = 10000

A = [ i for i in range(N) ]
B = list(A)
shuffle(B)

def quick_sort_inplace(S, low, high):
    if low >= high:
        return

    p = S[high] # choose last element as pivot
    i = low
    j = high - 1

    while i <= j:
        while S[i] < p and i <= j:
            i += 1
        while S[j] > p and i <= j:
            j -= 1

        if i <= j:
            S[i], S[j] = S[j], S[i] # swap elements
            i, j = i + 1, j - 1

    S[i], S[high] = S[high], S[i] # swap pivot

    quick_sort_inplace(S, low, i - 1)
    quick_sort_inplace(S, i + 1, high)

start = time()
quick_sort_inplace(B, 0, len(B) - 1)
end = time()
print(end - start)

assert A == B
