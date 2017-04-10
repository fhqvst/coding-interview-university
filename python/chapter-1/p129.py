def permute(chars):
    if len(chars) <= 1:
        yield chars
    else:
        for i in range(len(chars)):
            remaining = list(chars)
            remaining.pop(i)
            perms = permute(remaining)
            for perm in perms:
                yield [chars[i]] + perm

assert sum(1 for p in permute("a")) == 1
assert sum(1 for p in permute("aa")) == 2
assert sum(1 for p in permute("")) == 1
assert sum(1 for p in permute("catdog")) == 720
