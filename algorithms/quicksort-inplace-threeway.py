from random import shuffle
from time import time

N = 10000

A = [ i for i in range(N) ]
B = list(A)
shuffle(B)

def quick_sort_inplace(S, a, b):
    if a < b:
        pivot = S[b] # choose last element as pivot
        i, j, k = 0

        for n in range(a, b):
            if (S[i] == pivot):
                // Swap to middle
            elif (S[i] > pivot):
                // Swap to back


        while i <= j <= k <= b:

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

assert A == B
