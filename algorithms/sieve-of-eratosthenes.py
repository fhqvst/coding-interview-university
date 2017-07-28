def sieve(n):
    a = [True] * n
    a[0] = a[1] = False

    primes = []
    for (i, is_prime) in enumerate(a):
        if is_prime:
            primes.append(i)
            for j in range(i**2, n, i):
                a[j] = False

    return primes


assert sieve(10) == [2, 3, 5, 7]
assert sieve(21) == [2, 3, 5, 7, 11, 13, 17, 19]
