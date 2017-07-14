from random import shuffle
from time import time

N = 10000

A = [ i for i in range(N) ]
B = list(A)
shuffle(B)

def quick_sort(S):
  n = len(S)
  if (n < 2):
    return S

  pivot = S[0]
  L = []
  E = []
  G = []
  for i in S:
    if i < pivot:
      L.append(i)
    elif i == pivot:
      E.append(i)
    else:
      G.append(i)

  L = quick_sort(L)
  G = quick_sort(G)

  return L + E + G

start = time()
C = quick_sort(B)
end = time()
print(end - start)

assert A == C
