def sum_squares(n):
    value = 0
    for i in range(n):
        value += i**2
    return value

assert sum_squares(2) is 1
assert sum_squares(5) is 30
