from random import shuffle, randrange
from time import time

N = 10

A = [ i for i in range(N) ]
B = list(A)
shuffle(B)

def quick_sort_inplace(S, a, b):
    if a >= b:
        return


    p = randrange(a, b) # choose random element as pivot
    S[b], S[p] = S[p], S[b] # swap to last, then same as before
    pivot = S[b]
    left = a
    right = b - 1

    while left <= right:
        while S[left] < pivot and left <= right:
            left += 1
        while S[right] > pivot and left <= right:
            right -= 1

        # if pointers stop without having crossed each other it means we have
        # found a pair of elements which are out of order
        if left <= right:
            S[left], S[right] = S[right], S[left] # swap elements
            left, right = left + 1, right - 1

    S[left], S[b] = S[b], S[left] # swap pivot (S[b]) and left pointer (which is now actually to the right)

    quick_sort_inplace(S, a, left - 1)
    quick_sort_inplace(S, left + 1, b)

start = time()
quick_sort_inplace(B, 0, len(B) - 1)
end = time()
print(end - start)

try:
    assert A == B
except:
    print(A)
    print(B)
