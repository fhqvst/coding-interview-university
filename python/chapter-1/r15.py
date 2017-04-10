def sum_squares(n):
    return sum([ i**2 for i in range(n) ])

assert sum_squares(2) is 1
assert sum_squares(5) is 30
