#Describe a recursive algorithm to compute the integer part of the base-two logarithm of n using only addition and integer division.

def compute_int_log(n):
    if n < 2: return 0
    return 1 + compute_int_log(n / 2)

assert compute_int_log(10) == 3
assert compute_int_log(2) == 1
assert compute_int_log(31) == 4
