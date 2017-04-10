def permutations(chars):
    if len(chars) <= 1:
        yield chars
    else:
        for string in permutations(chars[1:]):
            


assert len(possible_strings("catdog".split()) is 720
