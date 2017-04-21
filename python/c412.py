def product(m, n, sum):
    if n == 0: return sum
    return product(m, n - 1, m + sum)

assert product(1, 2, 0) == 2
assert product(7, 8, 0) == 56
