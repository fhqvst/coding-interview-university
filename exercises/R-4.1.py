# Describe a recursive algorithm fro finding the maxmium element in a sequence, S, of n elements.

def find_max(sequence):
    return find_max_recurse(sequence, None)    

def find_max_recurse(sequence, max_value):
    if len(sequence) == 0:
        return max_value
    value = sequence.pop()
    return find_max_recurse(sequence, max(max_value if max_value else value, value))


assert find_max([1,5,3,6,0]) is 6

assert find_max([]) is None
