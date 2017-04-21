# Describe an efficient recursive function for solving the element uniqueness problem, which runs in time that is at most O(n^2) in the worst case without using sorting.

def is_unique(arr, i):
    if i == len(arr): return True
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]: return False
    return is_unique(arr, i + 1)

assert is_unique([1, 2, 3, 4, 5], 0)
assert not is_unique([1, 1, 2, 3], 0)
assert is_unique([3, 28, 99, 1000, 99999999999999, -57, 1, 0], 0)
