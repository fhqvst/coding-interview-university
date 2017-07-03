def find_min_max(arr, i, min, max):
    if i == len(arr) - 1: return (min, max)

    if min is None or arr[i] < min: min = arr[i]
    elif max is None or arr[i] > max: max = arr[i]

    return find_min_max(arr, i + 1, min, max)

assert find_min_max([2, 0, -1, 57, 58, 19], 0, None, None) == (-1, 58)
