def count_words(words):
    counter = dict()
    words = words.split()
    for w in words:
        counter[w] = counter.setdefault(w, 0) + 1

    return counter

assert count_words("hello my baby hello my honey").get("hello") is 2
assert count_words("hello my baby hello my honey").get("kevin", 0) is 0
