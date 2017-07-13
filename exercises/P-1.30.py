def times_until_max_two(n):
    if n <= 2:
        raise ValueException()

    times = 0
    while n >= 2:
        n = n / 2
        times += 1

    return times

assert times_until_max_two(4) == 2
assert times_until_max_two(5) == 2
assert times_until_max_two(17) == 4
