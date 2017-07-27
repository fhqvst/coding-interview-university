from array import array
import math

def _find_primes(m):
    print(m)
    if m <= 2:
        return [2]

    A = [True] * m
    small_primes = _find_primes(int(math.sqrt(2 * m)))
    for s in small_primes:
        for a in range(len(A)):
            if (m + a) % s == 0:
                A[a] = False
    primes = [ m + a for a in range(len(A)) if A[a] ]
    print(small_primes + primes)
    return small_primes + primes

def find_primes(m):
    return [ p for p in _find_primes(m) if p >= m ]

# assert find_primes(10) == [11, 13, 17, 19]
# assert find_primes(20) == [23, 29, 31, 37]
assert find_primes(100) == [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
