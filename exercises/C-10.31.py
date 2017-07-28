def sieve(m):
    A = [True] * 2 * m
    A[0] = A[1] = False
    
    primes = []
    for (i, is_prime) in enumerate(A):
        if is_prime:
            primes.append(i)
            for j in range(i**2, 2 * m, i):
                A[j] = False
    
    return [ p for p in primes if m <= p <= (2 * m) ]

assert sieve(10) == [11, 13, 17, 19]
assert sieve(20) == [23, 29, 31, 37]
assert sieve(100) == [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
